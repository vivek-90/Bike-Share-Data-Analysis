import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\nWould you like to see the data for Chicago, New York City or Washington?\n').title()
        if city == 'Chicago' or city == 'New York City' or city == 'Washington':
            break
        else:
            print ("Invalid city!!")

    while True:
        choice = input('Would you like to filter the data by month, day or none at all(Month, day, none):').title()
        if choice == 'None' or choice == 'Day' or choice =='Month':
            break
        else:
            print ('Invalid Input!!')

    if choice == 'Month':
        while True:
            month = input('\nWould you like to see the data for all, january, february, March, April, May, June?\n').title()
            if month == 'All' or month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June':
                day = 'All'
                break
            else:
                print ("Invalid month!!")

    elif choice == 'Day':
        while True:
            day = input('\nWhich day? please type in your reponse as (Sunday, Monday)\n').title()
            if day == 'Sunday' or day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday':
                month = 'All'
                break
            else:
                print ("Invalid day!!")

    elif choice == 'None':
        while True:
            month = 'All'
            day = 'All'
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month != 'All':
        months = ['January','February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

        # display the most common month
    popular_month = df['month'].mode()[0]
    count_month = df['month'].value_counts()[popular_month]
    print("Most frequent month of travel: ", popular_month)
    print("Number of times travelled during the month: ", count_month)

        # display the most common day of week
    popular_week = df['day_of_week'].mode()[0]
    count_week = df['day_of_week'].value_counts()[popular_week]
    print("Most frequent week of travel: ", popular_week)
    print("Number of times travelled during the week: ", count_week)

        # display the most common start hour

    popular_hour = df['hour'].mode()[0]
    count_hour = df['hour'].value_counts()[popular_hour]
    print("Most frequent hour of travel: ", popular_hour)
    print("Number of times travelled during the hour: ", count_hour)

    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    count_start_station = df['Start Station'].value_counts()[popular_start_station]
    print ('Most common used start station: ', popular_start_station)
    print ('Number of times the station has been used: ', count_start_station)
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    count_end_station = df['End Station'].value_counts()[popular_end_station]
    print ('Most common used end station: ', popular_end_station)
    print ('Number of times the station has been used: ', count_end_station)

    # display most frequent combination of start station and end station trip
    popular_combination_station = df['Start Station'] + ' to ' + df['End Station']
    frequent_combination = popular_combination_station.describe()["top"]
    count_common_station = popular_combination_station.value_counts()[frequent_combination]
    print ('Most common used combination of station: ', frequent_combination)
    print ('Number of times the combination of station has been used: ', count_common_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total trip duration is: ', travel_time)

    # display mean travel time
    mean_time = df['Trip Duration'].describe()["mean"]
    print('Average trip duration is: ', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_usertype = df['User Type'].value_counts()
    print ('\nThe no.of user types:\n', count_usertype)

    # Display counts of gender
    if city == 'Washington':
        print("The gender count data for Washington is not available")
    else:
        count_gender = df['Gender'].value_counts()
        print ('\nThe male to female count:\n', count_gender)

    # Display earliest, most recent, and most common year of birth
    if city == 'Washington':
        print("The year of birth data for Washington is not available")
    else:
        youngest = df['Birth Year'].describe()['max']
        oldest = df['Birth Year'].describe()['min']
        common_birthyear = df['Birth Year'].mode()[0]
        print('\nWhat is the oldest, youngest and common year of birth: \n', oldest, youngest, common_birthyear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
