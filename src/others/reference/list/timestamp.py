import datetime
from time import sleep


class TimestampedList:
    @staticmethod
    def add_timestamp(data_list, max_age=10):
        """Adds a timestamp to the list and removes items older than `max_age` seconds.

        Args:
            data_list: A list of data items or timestamps.
            max_age: Maximum age of items in the list in seconds (default is 10).

        Returns:
            A new list containing the timestamps (updated with the new timestamp).
        """

        current_time = datetime.datetime.now()
        new_timestamped_list = []

        # Add the new timestamp
        new_timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')
        new_timestamped_list.append(new_timestamp)

        # Filter existing timestamps, keeping only those within max_age
        filtered_timestamps = [timestamp for timestamp in data_list if (
            current_time - datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        ).total_seconds() <= max_age]

        # Combine the new timestamp with the filtered existing ones
        new_timestamped_list.extend(filtered_timestamps)

        print('New timestamped list:', new_timestamped_list)
        return new_timestamped_list


# Example usage:
data_list = []
for _ in range(5):  # Add 5 timestamps with 3-second intervals
    data_list = TimestampedList.add_timestamp(data_list)
    sleep(3)

# Print the final list containing all timestamps (including the new ones)
print(data_list)