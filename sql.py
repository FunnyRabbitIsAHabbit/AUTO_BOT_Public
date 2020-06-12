import mysql.connector
import datetime
from calculate import Future
from config import user, password, host, database


class DataBase:
    def __init__(self, data_user, data_password, data_host, data_database):
        self.user = data_user
        self.password = data_password
        self.host = data_host
        self.database = data_database

    def connection(self):
        connection = mysql.connector.connect(user=self.user,
                                             password=self.password,
                                             host=self.host,
                                             database=self.database)
        return connection, connection.cursor()

    def add_user(self, name, chat_id, email='NULL', _password='NULL', phone='NULL'):
        conn, cursor = self.connection()
        reg_time = datetime.datetime.now()
        reg_time = reg_time.strftime("%Y-%m-%d %H:%M:%S")
        to_exec = f"""insert into users (email, name, password, phone, registered_at_time, chat_id) values 
('{email}', '{name}', '{_password}', '{phone}', '{reg_time}', '{chat_id}')"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def add_car(self, user_id, brand='NULL', model='NULL', year='NULL'):
        conn, cursor = self.connection()
        to_exec = f"""insert into cars(user_id, brand, model, year) values
('{user_id}', '{brand}', '{model}', {year})"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def add_now(self, car_id):
        conn, cursor = self.connection()
        to_exec = f"""insert into nowcars(car_id) values
                ({car_id})"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def add_future(self, car_id):
        conn, cursor = self.connection()
        to_exec = f"""insert into futurecars(car_id) values
        ('{car_id}')"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def oil_update(self, car_id, oil):
        conn, cursor = self.connection()
        update_now = f"""update nowcars set oil = '{oil}' where car_id = {car_id}"""
        cursor.execute(update_now)
        future_oil = Future.oil(oil)
        update_future = f"""update futurecars set oil = '{future_oil}' where car_id = {car_id}"""
        cursor.execute(update_future)
        conn.commit()
        conn.close()
        cursor.close()

    def filter_update(self, car_id, filtr):
        conn, cursor = self.connection()
        update_now = f"""update nowcars set filter = '{filtr}' where car_id = {car_id}"""
        cursor.execute(update_now)
        future_filtr = Future.filtr(filtr)
        update_future = f"""update futurecars set filter = '{future_filtr}' where car_id = {car_id}"""
        cursor.execute(update_future)
        conn.commit()
        conn.close()
        cursor.close()

    def insurance_update(self, car_id, insurance):
        conn, cursor = self.connection()
        update_now = f"""update nowcars set insurance = '{insurance}' where car_id = {car_id}"""
        cursor.execute(update_now)
        future_insurance = Future.insurance(insurance)
        update_future = f"""update futurecars set insurance = '{future_insurance}' where car_id = {car_id}"""
        cursor.execute(update_future)
        conn.commit()
        conn.close()
        cursor.close()

    def tech_check_update(self, car_id, tech_check):
        conn, cursor = self.connection()
        update_now = f"""update nowcars set tech_check = '{tech_check}' where car_id = {car_id}"""
        cursor.execute(update_now)
        future_tech_check = Future.tech_check(tech_check)
        update_future = f"""update futurecars set tech_check = '{future_tech_check}' where car_id = {car_id}"""
        cursor.execute(update_future)
        conn.commit()
        conn.close()
        cursor.close()

    def air_tires_update(self, car_id, air_tires):
        conn, cursor = self.connection()
        update_now = f"""update nowcars set air_tires = '{air_tires}' where car_id = {car_id}"""
        cursor.execute(update_now)
        future_air_tires = Future.air_tires(air_tires)
        update_future = f"""update futurecars set air_tires = '{future_air_tires}' where car_id = {car_id}"""
        cursor.execute(update_future)
        conn.commit()
        conn.close()
        cursor.close()

    def update_car_model(self, user_id, param_value):
        conn, cursor = self.connection()
        to_exec = f"""update cars set model = '{param_value}' where user_id = '{user_id}'"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def update_car_brand(self, user_id, param_value):
        conn, cursor = self.connection()
        to_exec = f"""update cars set brand = '{param_value}' where user_id = '{user_id}'"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def update_car_year(self, user_id, param_value):
        conn, cursor = self.connection()
        to_exec = f"""update cars set year = '{param_value}' where user_id = '{user_id}'"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def update_user_city(self, username, param_value):
        conn, cursor = self.connection()
        to_exec = f"""update users set city = '{param_value}' where name = '{username}'"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def update_user_email(self, username, param_value):
        conn, cursor = self.connection()
        to_exec = f"""update users set email = '{param_value}' where name = '{username}'"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def update_user_password(self, username, param_value):
        conn, cursor = self.connection()
        to_exec = f"""update users set password = '{param_value}' where name = '{username}'"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def update_user_phone(self, username, param_value):
        conn, cursor = self.connection()
        to_exec = f"""update users set phone = '{param_value}' where name = '{username}'"""
        cursor.execute(to_exec)
        conn.commit()
        conn.close()
        cursor.close()

    def get_user_city(self, username):
        """

        :param username: str
        :return: str
        """

        conn, cursor = self.connection()
        to_exec = f"""select city from users where name = '{username}'"""
        cursor.execute(to_exec)
        records = cursor.fetchall()
        conn.close()
        cursor.close()

        return records[0][0]

    def get_user_city_by_chat(self, chat_id):
        """

        :param chat_id: str
        :return: str
        """

        conn, cursor = self.connection()
        to_exec = f"""select city from users where chat_id = '{chat_id}'"""
        cursor.execute(to_exec)
        records = cursor.fetchall()
        conn.close()
        cursor.close()

        return records[0][0]

    def select(self, table, columns):
        """

        :param table: str
        :param columns: list
        :return: list
        """
        conn, cursor = self.connection()
        to_exec = f"""select {','.join(columns)} from {table}"""
        cursor.execute(to_exec)
        records = cursor.fetchall()
        conn.close()
        cursor.close()

        return records

    def get_user_id(self, username):
        """

        :param username: str
        :return: str
        """

        conn, cursor = self.connection()
        to_exec = f"""select id from users where name = '{username}'"""
        cursor.execute(to_exec)
        records = cursor.fetchall()
        conn.close()
        cursor.close()

        return records[0][0]

    def get_user_id_by_chat(self, chat_id):
        """

        :param chat_id: str
        :return: str
        """

        conn, cursor = self.connection()
        to_exec = f"""select id from users where chat_id = '{chat_id}'"""
        cursor.execute(to_exec)
        records = cursor.fetchall()
        conn.close()
        cursor.close()

        return records[0][0]

    def get_car_id(self, user_id):
        """

        :param user_id: str
        :return: str
        """

        conn, cursor = self.connection()
        to_exec = f"""select id from cars where user_id = '{user_id}'"""
        cursor.execute(to_exec)
        records = cursor.fetchall()
        conn.close()
        cursor.close()

        return records[0][0]

    def get_car_notification(self, car_id):
        conn, cursor = self.connection()
        columns = ['oil', 'filter', 'insurance', 'tech_check', 'air_tires']
        to_exec = f"""select {','.join(columns)} from futurecars where car_id = '{car_id}'"""
        cursor.execute(to_exec)
        records = cursor.fetchall()
        conn.close()
        cursor.close()

        return dict(zip(columns, records[0]))

    def get_chat_ids(self):
        conn, cursor = self.connection()
        to_exec = f"""select chat_id from users"""
        cursor.execute(to_exec)
        records = cursor.fetchall()
        conn.close()
        cursor.close()

        return records[0]
