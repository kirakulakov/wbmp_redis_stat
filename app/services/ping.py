import datetime


class PingService:
    async def get_current_server_time(self) -> str:
        current_time = datetime.datetime.now()
        return current_time.strftime('%H:%M:%S')
