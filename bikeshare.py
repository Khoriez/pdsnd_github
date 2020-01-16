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
    city = str(input("Please enter a city between this cities 'chicago, new york city, washington' : "))
    while (city.lower() not in ['chicago','new york city','washington']):
        city = str(input("Please Re-enter a city between this cities 'chicago, new york city, washington' : "))
    city=city.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("Please enter a month between (all, january, february, ... , june): "))

    while (month.lower() not in ['all','january','february','march','april','may','june']):
        month = str(input("Please Re-enter a month or all "))
    month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("Please enter an day or all Ex:(all, monday, tuesday, ... sunday): "))
    while (day.lower() not in ['all', 'friday', 'sunday', 'saturday', 'monday','tuesday', 'wednesday', 'thursday']):
        day = str(input("Please Re-enter a day or all "))
    day =day.lower()

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
    num_month = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    num_day = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'sunday': 5, 'saturday': 6}
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        df = df[(df['Start Time'].dt.month == num_month[month])]
        if day != 'all':
                df = df[(df['Start Time'].dt.weekday == num_day[day])]
    else:
        if day != 'all':
                df = df[(df['Start Time'].dt.weekday == num_day[day])]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    num_day_dict = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'sunday', 6: 'saturday'}
    num_month_dict = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june'}
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # TO DO: display the most common month
    print("the most common month : {}".format(num_month_dict[df['Start Time'].dt.month.mode()[0]]))

    # TO DO: display the most common day of week
    print("the most common day of week : {}".format(num_day_dict[df['Start Time'].dt.weekday.mode()[0]]))

    # TO DO: display the most common start hour
    print("the most common  start hour : {}".format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly used start station is {}".format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print("the most commonly used end station is {}".format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    station_couple = df['Start Station'] + ' --> ' + df['End Station']
    print("the most frequent combination of start station and end station trip is {}".format(station_couple.value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    travel_time=df['End Time']-df['Start Time']
    # TO DO: display total travel time
    print('The total travel time is {} :'.format(travel_time.sum()))
    # TO DO: display mean travel time
    print('The mean travel time is {} :'.format(travel_time.mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types are \n{}: '.format(df['User Type'].value_counts()))
    # TO DO: Display counts of gender
    if 'Gender' in df :
        print('Counts of gender : \n{}: '.format(df['Gender'].value_counts()))
    else:
        print("Oops This data didn't contain the gender of users ")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df :

        print('The earliest  year of birth is {} '.format(int(list(df['Birth Year'].dropna(axis = 0).sort_values())[-1])))
        print('The most recent  year of birth is {} '.format(int(list(df['Birth Year'].dropna(axis = 0).sort_values())[0])))
        print('The most common  year of birth is {} '.format(int(df['Birth Year'].value_counts().idxmax())))
    else:
        print("Oops This data didn't contain the birth year of users ")

    print("\nThis took %s seconds." % (time.time() - start_time))
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
