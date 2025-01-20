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

INSERT INTO faqs (question, answer) VALUES (
	'What are your opening times',
    'We are open 24 hours a day, 7 days a week! So you can come in at any time that is most convenient for you! Whether you’re normal and you like to workout during the busy evening hours, or you’re weird and you like to workout at midnight, our perpetual open hours prove to be very convenient!'
);

INSERT INTO faqs (question, answer) VALUES (
	'Are there storage facilities available',
    'Of course! We have over 100 lockers in the changing rooms, and we provide padlocks to help keep your belongings secure. We also have lockers available to rent monthly in the event you wanted to store your things in the gym for longer than your workout session.'
);

INSERT INTO faqs (question, answer) VALUES (
	'How much is a gym membership',
    'Very affordable! Only £29.99 per month, with no joining fees, contracts or commitments required! Simply pay a monthly subscription made via direct debit and enjoy 24/7 access to all our facilities!'
);

INSERT INTO faqs (question, answer) VALUES (
	'Do you have good workout machines',
    'All of our workout machines are state-of-the-art equipment, made by trusted and certified brands! They are regularly inspected and maintained to ensure that they are up to operational standard and are safe for use!'
);

INSERT INTO faqs (question, answer) VALUES (
	'Is there a car park',
    "Yes! We have a large car park with over 100 parking spots. And it's free too! We also have a cycle rack available for those who prefer to commute on two wheels, with a rain shield to protect it from the weathery elements!"
);

INSERT INTO faqs (question, answer) VALUES (
	'Are there any personal training services available',
    'Yes! We have personal trainers working every Monday to Friday who are there to help you with your fitness goals! Once you become a member, you are able to book appointments with our PTs for one-on-one sessions!'
);

INSERT INTO faqs (question, answer) VALUES (
	'Do you supply supplements',
    'We have vending machines throughout the gym that supply basic things for your workout e.g. preworkout, energy drinks to power you through your workout, BCAA drinks, as well as post workout protein shakes!'
);

INSERT INTO exercise_types VALUES ('Biceps');
INSERT INTO exercise_types VALUES ('Triceps');
INSERT INTO exercise_types VALUES ('Upper Back');
INSERT INTO exercise_types VALUES ('Lower Back');
INSERT INTO exercise_types VALUES ('Shoulders');
INSERT INTO exercise_types VALUES ('Quads');
INSERT INTO exercise_types VALUES ('Hamstrings');
INSERT INTO exercise_types VALUES ('Calves');
INSERT INTO exercise_types VALUES ('Cardio');
INSERT INTO exercise_types VALUES ('Crossfit');

INSERT INTO exercises VALUES (
	'Preacher Curls',
    'Biceps',
    'A classic bicep isolation exercise that locks your arms in a fixed position, ensuring strict form and maximum engagement of the biceps. Perfect for building strength, size, and a defined bicep peak, this move eliminates momentum, allowing you to focus on controlled, effective reps.'
);

INSERT INTO exercises VALUES (
	'Bayesian Curls', 
    'Biceps', 
    'A modern twist on bicep training that combines constant tension with a full range of motion. By anchoring a cable behind you and curling with a slight forward lean, this exercise maximizes stretch and contraction, targeting the biceps for optimal growth and definition while reducing joint stress.'
);

INSERT INTO exercises VALUES (
	'Hammerhead Curls', 
    'Biceps', 
    'A versatile bicep and forearm builder that targets the brachialis for thicker, stronger arms. With a neutral grip, this exercise emphasizes arm strength, adds width to your biceps, and supports overall upper-body stability, making it a staple for well-rounded arm development.'
);

INSERT INTO exercises VALUES (
	'Triceps Dips', 
    'Triceps', 
    'A bodyweight classic for building bigger, stronger triceps. By lowering and raising your body between parallel bars or on a bench, this exercise emphasizes the long head of the triceps while engaging your chest and shoulders for a powerful upper-body workout.'
);

INSERT INTO exercises VALUES (
	'Overhead Tricep Extensions', 
    'Triceps', 
    'The ultimate stretch-and-squeeze move for long head tricep development. Holding a dumbbell or cable overhead, this exercise enhances muscle length and shape, promoting balanced, defined arms'
);

INSERT INTO exercises VALUES (
	'Face Pulls', 
    'Upper Back', 
    'A must-do for upper back and shoulder health. Using a cable or resistance band, this exercise strengthens the rear delts, traps, and rotator cuff muscles, promoting posture, stability, and balanced shoulder development.'
);

INSERT INTO exercises VALUES (
	'Pullups', 
    'Upper Back', 
    'The ultimate bodyweight move for building a wide, strong upper back. By pulling your chest to the bar, this exercise targets the lats, traps, and rear delts, enhancing back width and overall upper-body strength.'
);

INSERT INTO exercises VALUES (
	'Back Extension', 
    'Lower Back', 
    'A targeted isolation exercise for strengthening the lower back and spinal erectors. Performed on a hyperextension bench or Roman chair, this move enhances lower back endurance, protects against injury, and improves overall core stability.'
);

INSERT INTO exercises VALUES (
	'Deadlifts', 
    'Lower Back', 
    'The king of all lifts for building a strong, resilient lower back. This compound exercise engages the spinal erectors, glutes, and hamstrings, improving posture, stability, and full-body strength with every rep.'
);

INSERT INTO exercises VALUES (
	'Lateral Raises', 
    'Shoulders', 
    'The ultimate isolation exercise for wider, more defined shoulders. By lifting dumbbells to the sides with controlled form, this move hones in on the lateral delts, creating a broader, more athletic look.'
);

INSERT INTO exercises VALUES (
	'Overhead Press', 
    'Shoulders', 
    'A powerhouse compound movement for building strong, sculpted shoulders. Pressing a barbell or dumbbells overhead targets the delts while engaging the triceps and upper chest for balanced upper-body strength and size.'
);

INSERT INTO exercises VALUES (
	'Barbell Squats', 
    'Quads', 
    'The king of leg exercises, building strength, size, and power in your quads, glutes, and hamstrings. By lowering into a deep squat and driving back up, this compound movement activates your entire lower body and core for maximum muscle development.'
);

INSERT INTO exercises VALUES (
	'Leg Press', 
    'Quads', 
    'A quad-dominant machine exercise that allows you to push heavy weights safely. By pressing the platform away from your body, this move targets the quads, glutes, and hamstrings while minimizing stress on your lower back.'
);

INSERT INTO exercises VALUES (
	'Romanian Deadlifts (RDLs)', 
    'Hamstrings', 
    'A hamstring-focused powerhouse that emphasizes the stretch and contraction of the posterior chain. By lowering a barbell or dumbbells with a slight knee bend, this exercise builds strength, flexibility, and muscle in the hamstrings and glutes.'
);

INSERT INTO exercises VALUES (
	'Lying Leg Curls', 
    'Hamstrings', 
    'A targeted isolation exercise for hamstring growth and strength. Performed on a machine, this movement emphasizes the contraction phase, ensuring maximum engagement for building balanced and powerful legs.'
);

INSERT INTO exercises VALUES (
	'Standing Calf Raises', 
    'Calves', 
    'A classic exercise for building strong, defined calf muscles. By lifting your heels off the ground while standing, this move targets the gastrocnemius for size and power, creating a well-rounded lower leg.'
);

INSERT INTO exercises VALUES (
	'Seated Calf Raises', 
    'Calves', 
    'The go-to exercise for isolating and strengthening the soleus muscle in your calves. Performed with a seated machine or free weights, this move enhances endurance, definition, and lower leg stability.'
);

INSERT INTO exercises VALUES (
	'Treadmill', 
    'Cardio', 
    'A versatile cardio machine for walking, jogging, or running at your own pace. It’s perfect for improving cardiovascular endurance, burning calories, and building lower-body strength with customizable speed and incline settings.'
);

INSERT INTO exercises VALUES (
	'Stair Master', 
    'Cardio', 
    'The ultimate cardio workout for building leg strength and endurance. By mimicking stair climbing, this machine targets your glutes, quads, and calves while boosting your heart rate, making it an efficient calorie burner and muscle toner.'
);

INSERT INTO exercises VALUES (
	'Burpees', 
    'Crossfit', 
    'A high-intensity CrossFit classic that works your entire body. By combining a push-up, squat, and jump, this exercise boosts endurance, burns fat, and builds strength, making it a go-to for functional fitness.'
);

INSERT INTO exercises VALUES (
	'Thrusters', 
    'Crossfit', 
    'A dynamic CrossFit staple that combines a front squat and an overhead press. This full-body exercise builds explosive power, targets the legs, core, and shoulders, and torches calories for an intense strength and cardio workout.'
);

INSERT INTO equipment VALUES (
	'Squat Rack',
    "We have several squat racks available at our gym! With multiple levels and barbels of varying weights, as well as several free weights, you can easily adjust the required level so that you can squat as efficiently as you'd like! You can use these for box squats, overhead presses, barbell squats, and many more!",
    'https://i.postimg.cc/15GKqYGr/pexels-dubtastic-28320723.jpg',
    10
);

INSERT INTO equipment VALUES (
	'Bench Rack',
    'Use this to have the perfect bench press! With our adjustable back, you can also carry out incline bench presses as well at different angles. Use this machine to target various areas of your chest to build that perfect physique!',
    'https://i.postimg.cc/X7rbNd9W/2151114151.jpg',
    15
);

INSERT INTO equipment VALUES (
	'Kettlebell Weights',
    'We have a wide range of kettlebell weights of various colours, sizes and weights! Use these to build stability and grip strength, and as a safe means of carrying out more intense exercises!',
    'https://i.postimg.cc/CxDpk0v6/3d-gym-equipment-1.png',
    60
);

INSERT INTO equipment VALUES (
	'Pulldown Machines',
    "This is one of our machines that can be used to perform multiple exercises in one go, especially if you're a super setter! Use this to perform exercises like lat pulldowns, overhead triceps extensions as well as triceps pushdowns!",
    'https://i.postimg.cc/7Yjy5hN2/3d-gym-equipment.jpg',
    8
);

ALTER TABLE personal_trainers
ADD image_link VARCHAR(255) NOT NULL;

INSERT INTO personal_trainers VALUES (
	'Foad Shariyati',
    "I help clients achieve their ideal physique through tailored training programs and expert guidance. With a focus on hypertrophy, symmetry, and progressive overload, I design workouts to maximize muscle growth and strength. I emphasize proper form, effective recovery, and goal-specific nutrition to ensure sustainable results. Whether you're preparing for competition or building your dream body, I’m here to guide you every step of the way.",
    '2022-06-04',
    'shariyatifitness@gmail.com',
    '07291003928',
    'https://i.postimg.cc/gk7w2b84/pexels-foadshariyati-30206161-Copy.jpg'
);

INSERT INTO personal_trainers VALUES(
	'Cesar Geleao',
    "I help clients build strength and master the big three lifts: squat, bench press, and deadlift. My programs are tailored to improve technique, maximize power, and progressively increase lifting performance. With a focus on proper form, injury prevention, and recovery, I ensure safe and effective training. Whether you're competing or just aiming to lift heavier, I’m here to guide you every step of the way.",
    '2021-12-05',
    'gelion@fitnessbusiness.org',
    '07991820113',
    'https://i.postimg.cc/VNq5gSTH/pexels-cesar-galeao-1673528-3289711-Copy.jpg'
);

INSERT INTO personal_trainers VALUES (
	'Lucie Talling',
    "I focus on creating personalized fitness programs that help clients burn fat, build strength, and achieve sustainable results. By combining effective workouts with practical nutrition guidance, I ensure a balanced approach to reaching your goals. I prioritize proper form, accountability, and long-term habits to make your journey enjoyable and successful. Whether you're just starting or looking to break through a plateau, I’m here to guide and support you every step of the way.",
    '2023-05-10',
    'tellingontheweight@gmail.com',
    '07652019353',
    'https://i.postimg.cc/2yMzrmMZ/pexels-shkrabaanthony-4662359-Copy.jpg'
);