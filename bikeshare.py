import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = input("Would you like to analyze data for chicago, new york city, or washington?: ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("That's not a valid entry. Please select chicago, new york city, or washington: ")

    month = input("Please choose a month from january to june or all if you don't want to filter by month: ").lower()
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input("That's not a valid entry. Please select January, February, March, April, May, June, or all: ")

    day = input("Please enter a day of the week (e.g. monday) or all: ").lower()
    while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input("That's not a valid entry. Please select monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all: ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['month'].mode()
    print('Most popular month:', popular_month)

    popular_day_of_week = df['day'].mode()
    print('Most popular day:', popular_day_of_week)

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()
    print('Most popular hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('Most popular Start Station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print('Most popular End Station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = (df['Start Station'] + " to " + df['End Station'])
    popular_trip = df['trip'].mode()
    print('Most popular trip: ', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time, ' seconeds')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time: ', mean_travel_time, ' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('Gender Types: ', gender_types)
    else:
        print("Sorry, Washington does not have gender data")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        oldest_user = df['Birth Year'].min()
        youngest_user = df['Birth Year'].max()
        typical_user = df['Birth Year'].mode()
        print('Oldest Birth Year: ', oldest_user)
        print('Youngest Birth Year: ', youngest_user)
        print('Most Common Birth Year: ', typical_user)
    else:
        print("Sorry, Washington does not have birth year data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_preview(df):
    """Gives the option to view the dataset 5 rows at a time"""

    preview_select = input("Would you like to view 5 rows of this data set? (Y/N): ").lower()
    if preview_select in ('y', 'yes'):
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            more_data = input("Would like to see 5 more rows? (Y/N): ").lower()
            if more_data not in ('y', 'yes'):
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_preview(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
