/*this is where I will keep all code that has been executed*/
CREATE DATABASE gainz_center_database;

USE gainz_center_database;

CREATE TABLE users (
	username VARCHAR(225) PRIMARY KEY,
    person_name VARCHAR(225) NOT NULL,
    email VARCHAR(225) NOT NULL UNIQUE,
    mobile VARCHAR(255) NOT NULL UNIQUE,
    dob DATE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE faqs (
	id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
);

CREATE TABLE equipment (
	equipment_name VARCHAR(255) PRIMARY KEY,
    equipment_description TEXT NOT NULL,
    image_link VARCHAR(255) NOT NULL,
    quantitiy INT NOT NULL
);

CREATE TABLE exercise_types (
	type_name VARCHAR(255) PRIMARY KEY
);

CREATE TABLE personal_trainers (
	pt_name VARCHAR(255) PRIMARY KEY,
    introduction TEXT NOT NULL,
	date_started DATE NOT NULL,
	contact_email VARCHAR(255) NOT NULL,
	contact_phone VARCHAR(15) NOT NULL
);

CREATE TABLE exercises (
	exercise_name VARCHAR(255) PRIMARY KEY,
    type_name VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (type_name) REFERENCES exercise_types(type_name)
);

CREATE TABLE my_sessions (
	session_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    date_of_session DATE NOT NULL,
    pre_made INT NOT NULL, /*0 if it is just logged on the day, 1 if it was pre-planned but not yet attended, 2 if it was pre-planned and attended*/
    check_in_time DATETIME,
    check_out_time DATETIME,    
    FOREIGN KEY (username) REFERENCES users(username)
);

CREATE TABLE my_prs (
	pr_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    exercise_name VARCHAR(255) NOT NULL,
    session_id INT NOT NULL,
    pr_record INT NOT NULL,
    unit VARCHAR(255) NOT NULL,
    date_of_pr DATE NOT NULL,    
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (exercise_name) REFERENCES exercises(exercise_name),
    FOREIGN KEY (session_id) REFERENCES my_sessions(session_id)
);

CREATE TABLE session_exercises (
	id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    session_id INT NOT NULL,
    exercise_name VARCHAR(255) NOT NULL,
    set_number INT NOT NULL,
    reps INT NOT NULL,
    weight INT NOT NULL,
    unit VARCHAR(255) NOT NULL,    
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (session_id) REFERENCES my_sessions(session_id),
    FOREIGN KEY (exercise_name) REFERENCES exercises(exercise_name)
);

CREATE TABLE pt_sessions (
	session_id INT AUTO_INCREMENT PRIMARY KEY,
    pt_name VARCHAR(255) NOT NULL,
    booking_id INT,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_booked BOOLEAN NOT NULL,
    FOREIGN KEY (pt_name) REFERENCES personal_trainers(pt_name)
);

CREATE TABLE pt_bookings (
	booking_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    pt_name VARCHAR(255) NOT NULL,
    session_id INT NOT NULL,
    date_of_booking DATE NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (pt_name) REFERENCES personal_trainers(pt_name)
);

ALTER TABLE pt_sessions
ADD CONSTRAINT fk_booking_id
FOREIGN KEY (booking_id) REFERENCES pt_bookings(booking_id);

ALTER TABLE pt_bookings
ADD CONSTRAINT fk_session_id
FOREIGN KEY (session_id) REFERENCES pt_sessions(session_id);