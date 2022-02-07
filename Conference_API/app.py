import streamlit as st
import datetime
import requests, json
import pandas as pd

page =  st.sidebar.selectbox('choose your box', ['users', 'rooms','bookings'])

if page == 'users':
    st.title('Create_User')

    with st.form(key='user'):
        #user_id: int = random.randint(0, 10)
        username: str = st.text_input('User Name',max_chars=12)
        data = {
            #'user_id': user_id,
            'username': username
        }
        submit_botton = st.form_submit_button(label='Send Request')

    if submit_botton:
        #st.write('## Request Data')
        url='http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        st.write('## Respond Data')
        if res.status_code == 200:
            st.success("Create Users")
        st.json(res.json())

elif page == 'rooms':
    st.title('Room Registration')

    with st.form(key='room'):
        #room_id: int = random.randint(0, 10)
        roomname: str = st.text_input('Room Name',max_chars=12)
        capacity: int = st.number_input('Capacity',step=1)
        data = {
            #'room_id': room_id,
            'roomname': roomname,
            'capacity': capacity
        }
        submit_botton = st.form_submit_button(label='Registration')

    if submit_botton:
        url='http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('Complite Registration')
        st.json(res.json())

elif page == 'bookings':
    st.title('Booking Room')

    url_users = 'http://127.0.0.1:8000/users'
    res = requests.get(url_users)
    users = res.json()
    users_dict = {}
    for user in users:
        users_dict[user['username']] = user['user_id']
    
    url_rooms = 'http://127.0.0.1:8000/rooms'
    res = requests.get(url_rooms)
    rooms = res.json()
    rooms_dict = {}
    for room in rooms:
        rooms_dict[room['roomname']] = {
            'room_id': room['room_id'],
            'capacity': room['capacity']
        }
    st.write('### Room List')
    df_rooms = pd.DataFrame(rooms)
    st.table(df_rooms)

    with st.form(key='booking'):
        # booking_id: int = random.randint(0, 10)
        username: str = st.selectbox('User Name', users_dict.keys())
        roomname: str = st.selectbox('Room Name', rooms_dict.keys())
        booked_num: int = st.number_input('Number', step=1, min_value=1)
        date = st.date_input('Input date today', min_value=datetime.date.today())
        start_time = st.time_input('Input start time: ', value=datetime.time(hour=9, minute=0))
        end_time = st.time_input('Input end time: ', value=datetime.time(hour=20, minute=0))      
        submit_botton = st.form_submit_button(label='Send Request')

    if submit_botton:
        user_id: int = users_dict[username]
        room_id: int = rooms_dict[roomname]['room_id']
        capacity: int = rooms_dict[roomname]['capacity']

        data = {
            'user_id': user_id,
            'room_id': room_id,
            'booked_num': booked_num,
            'start_datetime': datetime.datetime(
                year=date.year,
                month=date.month,                     
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
            ),
            'end_datetime': datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute
            )
        }
        if booked_num <= capacity:
            url='http://127.0.0.1:8000/bookings'
            res = requests.post(
                url,
                data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success('Reservation confirmed')
            st.json(res.json())

        else:
            st.error(f'{roomname} needs {capacity} people')