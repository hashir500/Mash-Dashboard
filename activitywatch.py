import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class ActivityWatchClient:
    def __init__(self, host="localhost", port=5600):
        self.base_url = f"http://{host}:{port}/api/0"
        self.buckets_cache = None
    
    def test_connection(self) -> bool:
        """Test if ActivityWatch is running and accessible"""
        try:
            response = requests.get(f"{self.base_url}/buckets", timeout=2)
            return response.status_code == 200
        except:
            return False
    
    def get_buckets(self) -> Dict[str, Dict]:
        """Get all buckets from ActivityWatch"""
        if self.buckets_cache is not None:
            return self.buckets_cache
        
        try:
            response = requests.get(f"{self.base_url}/buckets", timeout=5)
            if response.status_code == 200:
                self.buckets_cache = response.json()
                return self.buckets_cache
        except Exception as e:
            print(f"Error fetching buckets: {e}")
        
        return {}
    
    def get_events(self, bucket_id: str, start: datetime, end: datetime) -> List[Dict]:
        """Get events from a bucket for a time range"""
        try:
            start_str = start.isoformat()
            end_str = end.isoformat()
            
            url = f"{self.base_url}/buckets/{bucket_id}/events"
            params = {
                "start": start_str,
                "end": end_str
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error fetching events from {bucket_id}: {e}")
        
        return []
    
    def get_window_events(self, start: datetime, end: datetime) -> List[Dict]:
        """Get window events (app/window usage)"""
        buckets = self.get_buckets()
        window_events = []
        
        for bucket_id, bucket_data in buckets.items():
            if bucket_data.get("type") in ["window-watcher", "currentwindow"]:
                events = self.get_events(bucket_id, start, end)
                window_events.extend(events)
        
        return window_events
    
    def get_browser_events(self, start: datetime, end: datetime) -> List[Dict]:
        """Get browser events (web browsing)"""
        buckets = self.get_buckets()
        browser_events = []
        
        for bucket_id, bucket_data in buckets.items():
            if bucket_data.get("type") == "browser":
                events = self.get_events(bucket_id, start, end)
                browser_events.extend(events)
        
        return browser_events
    
    def get_afk_events(self, start: datetime, end: datetime) -> List[Dict]:
        """Get AFK (Away From Keyboard) events"""
        buckets = self.get_buckets()
        afk_events = []
        
        for bucket_id, bucket_data in buckets.items():
            if bucket_data.get("type") in ["afkwatcher", "afkstatus"]:
                events = self.get_events(bucket_id, start, end)
                afk_events.extend(events)
        
        return afk_events
    
    def calculate_app_usage(self, start: datetime, end: datetime) -> Dict[str, int]:
        """Calculate total time spent in each app"""
        events = self.get_window_events(start, end)
        app_usage = {}
        
        for event in events:
            data = event.get("data", {})
            app_name = data.get("app", "Unknown")
            duration = event.get("duration", 0) / 60  # Convert seconds to minutes
            
            if app_name not in app_usage:
                app_usage[app_name] = 0
            app_usage[app_name] += duration
        
        return app_usage
    
    def calculate_total_time(self, start: datetime, end: datetime) -> int:
        """Calculate total active time (excluding AFK)"""
        afk_events = self.get_afk_events(start, end)
        
        total_active = 0
        for event in afk_events:
            data = event.get("data", {})
            status = data.get("status", "")
            if status == "not-afk":
                total_active += event.get("duration", 0)
        
        return int(total_active / 60)  # Convert to minutes
    
    def get_activity_timeline(self, start: datetime, end: datetime, limit: int = 20) -> List[Dict]:
        """Get activity timeline events"""
        events = self.get_window_events(start, end)
        
        # Sort by timestamp
        events.sort(key=lambda x: x.get("timestamp", ""))
        
        timeline = []
        for event in events[:limit]:
            data = event.get("data", {})
            app_name = data.get("app", "Unknown")
            title = data.get("title", "")
            timestamp = datetime.fromisoformat(event.get("timestamp", "").replace("Z", "+00:00"))
            
            timeline.append({
                "title": app_name,
                "subtitle": title[:50] if title else "Active",
                "timestamp": timestamp.strftime("%I:%M %p"),
                "date": timestamp.strftime("%Y-%m-%d")
            })
        
        return timeline
    
    def get_daily_heatmap_data(self, days: int = 365) -> Dict[str, int]:
        """Get heatmap data for the last N days"""
        end_date = datetime.now()
        heatmap_data = {}
        
        for i in range(days):
            date = end_date - timedelta(days=i)
            start = datetime(date.year, date.month, date.day)
            end = datetime(date.year, date.month, date.day, 23, 59, 59)
            
            total_time = self.calculate_total_time(start, end)
            
            # Map time to activity level (0-4)
            if total_time < 30:
                level = 0
            elif total_time < 120:
                level = 1
            elif total_time < 240:
                level = 2
            elif total_time < 360:
                level = 3
            else:
                level = 4
            
            heatmap_data[date.strftime("%Y-%m-%d")] = level
        
        return heatmap_data


# Global client instance
aw_client = ActivityWatchClient()
