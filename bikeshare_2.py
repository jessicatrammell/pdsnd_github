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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Please enter one of the following cities: Chicago, New York City or Washington.').lower()
    while city not in ('Chicago', 'New York City', 'Washington'):
        break
    else: 
        print('Please only enter Chicago, New York City OR Washington')
        
    # TO DO: get user input for month (all, january, february, ... , june)

    month = input("Please enter a month from January to June or simply enter all for all of the months.").lower()
    while month not in ['all', 'January', 'February', 'March', 'April', 'May', 'June']:
        break
    else: 
        print('Please try again')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Please enter a day of the week or all for the entire week.").lower()
    while day not in ['all', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
        break
    else: 
        print('Please try again')
        
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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the start time into datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month and day of week from Start time in new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    
    #filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day
    if day != 'all':
        
        #filter by day to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Commonly used start station:', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Commonly used end station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = (df['Start Station'] + '-' + df['End Station']).mode()[0]
    print('Most commonly used start and end stations:', combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum() / 3600
    print("total travel time in hours is: ", total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean() / 3600
    print("mean travel time in hours is: ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    if 'Gender' in df.columns:
  
    # TO DO: Display counts of gender
        user_gender = df['Gender'].value_counts()
        print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = int(df['Birth Year'].min())
        print('Earliest Year:', earliest_birth)
        most_recent_birth = int(df['Birth Year'].max())
        print('Most Recent Year:', most_recent_birth)
        most_common_year_of_birth = int(df['Birth Year'].value_counts().mode()[0])
        print('Most Common Year:', most_common_year_of_birth)
                                    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    i = 0
    
    while True:
        raw_data = input('Would you like to see some raw data? Please enter Yes or No.')
        if raw_data.lower() == 'yes':
            print(df[i:i+5])
            i += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        else: 
                print('Your answer is invalid. Please enter yes or no.')

if __name__ == "__main__":
	main()
