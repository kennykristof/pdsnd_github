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
    while True:        
 city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower() 
 if city not in ('chicago', 'new york city', 'washington'):         
  print('Incorrect city. Please try again!\n')            
  continue
 else:
  break
    # TO DO: get user input for month (all, january, february, ... , june)
     while True:        
 month = input('Would you like to see data for January, February, March, April, May, June, or all?\n').lower()
 if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):         
  print('Incorrect month. Please try again!\n')            
  continue
 else:
  break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:        
        day = input('Would you like to see data for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\n').lower()
 if day not in ('monday', 'tuesday','wednesday','thursday','friday','saturday','sunday','all'):
  print('Incorrect day. Please try again!\n')       
  continue
 else:
  break
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
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
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df = pd.read_csv(CITY_DATA[city])
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('The most common month is\n' most_common_month)
    
    # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.week
    most_common_week = df['week'].mode()[0]
    print('The most common week is\n' most_common_week)
        
    # TO DO: display the most common start hour
    df['week'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is\n' most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])
    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0] 
    print('The most commonly used start station is\n' most_common_start_station)
    
    # TO DO: display most commonly used end station
    most_common_start_station = df['End Station'].mode()[0] 
    print('The most commonly used end station is\n' most_common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print('The most frequent combination is\n' popular_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])
    # TO DO: display total travel time
    total_travel = df.sum('Trip Duration')
    print('The total travel time is\n' total_travel)
    # TO DO: display mean travel time
    mean_travel = df.mean('Trip Duration)
    print('The mean travel time is\n' mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    df = pd.read_csv(CITY_DATA[city])
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The dispersion of user types is\n' user_types)
    # TO DO: Display counts of gender
    genders = df['Gender'].value_counts()
    print('The dispersion of genders is\n'genders)
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()[0]
    print('The most earliest year of birth is\n' earliest_birth)            
    print('The most recent year of birth is\n' recent_birth)
    print('The most common year of birth is\n' most_common_birth)
    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


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


if __name__ == "__main__":
	main()
