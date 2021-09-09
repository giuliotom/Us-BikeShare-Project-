import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
    city = ''

    while city not in CITY_DATA.keys():
        print('Please Choose a city:')
        print('-Chicago \n-New York City \n-Washington')
        city = input('Choose the city you want to explore:').lower()

        if city not in CITY_DATA.keys():
            print('Please check your input')


    print('You have choosen ', city.title(), '!')





    # TO DO: get user input for month (all, january, february, ... , june)
    MONTHS ={'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTHS.keys():
        print('Please choose a month:')
        print('-January \n-February \n-March \n-April \n-May \n-June \n-All')
        month = input('Choose the month you want to explore:').lower()


        if month not in MONTHS.keys():
            print('Please check your input')

        else:
            print('You have choosen ', month.title(), '!')






    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAYS = { 'sunday':1, 'monday': 2, 'tuesday': 3, 'wednesday': 4, 'thursday': 5, 'friday': 6, 'saturday': 7, 'all': 8}
    day = ''

    while day not in DAYS.keys():
        print('Please choose a day:')
        print('-Sunday \n-Monday \n-Tuesday \n-Wednesday \n-Thursday \n-Friday \n-Saturday \n-All')
        day = input('Choose the day you want to explore:').lower()

        if day not in DAYS.keys():
            print('Please check your input')
        else:
            print('You have choosen ', day.title(), '!')



        print('-'*40)
    return(city, month, day)



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
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month = df['Month'].mode()[0]
    print(f'Most popular month (Jan = 1,..., June = 6) is:  {pop_month}')


    # TO DO: display the most common day of week
    pop_day = df['Day'].mode()[0]
    print(f'Most popular day is:  {pop_day}')


    # TO DO: display the most common start hour
    pop_hour = df['Hour'].mode()[0]
    print(f'Most popular hour is:  {pop_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print(f'The most comonly used start station is: {pop_start_station}')

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print(f'The most comonly used end station is:  {pop_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + df['End Station']
    combination = df['Start to End'].mode()[0]
    print(f'Most frequent combination of start station and end station trip is:  {combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_duration = df['Trip Duration'].sum()
    minute, second = divmod(tot_duration, 60)
    hour, minute = divmod(minute, 60)
    print(f'The total trip duration is {hour} hours, {minute} minutes and {second} seconds.')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean travel time is: {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users = df['User Type'].value_counts()
    print(f'Types of user by number:  {count_users}')

        # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender_count = df['Gender'].value_counts()
        print(f'Users by gender are:  \n{gender_count}' )

    else:
        print('There is no Gender column here..')

        # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print(f'Earliest year of birth is:  {earliest}', f'\nMost recent year of birth is:  {most_recent}', f'\nMost common year of birth is: {common}')

    else:
        print('There is no Birth Year column here..')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data
        Return:
               None
    """
    print(df.head())
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 more rows of individual trip data? Enter yes or no\n')
        if view_data.lower() != 'yes':
            return
        start_loc +=  5
        print(df.iloc[start_loc:start_loc+5])
        break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            if view_data.lower() != 'yes':
                break
            raw_data(df)
            break




        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
    main()
