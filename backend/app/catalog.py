"""Entirely fictional PEERLINK seminar dataset."""
TOPICS = {
 "Mathematics": ["Quadratic Equations", "Algebra", "Statistics"],
 "English": ["Grammar", "Essay Writing"],
 "Science": ["Biology", "Chemistry"],
 "Filipino": ["Panitikan", "Pagsulat"],
}
SLOTS = ["Wednesday 3 PM", "Thursday 4 PM", "Friday 2 PM", "Monday 3 PM"]
TUTORS = [
 {"id":"t1","account_id":"joshua","name":"Joshua Reyes","grade":11,"subject":"Mathematics","topics":["Quadratic Equations","Algebra"],"slots":["Wednesday 3 PM","Friday 2 PM"],"eligible":True},
 {"id":"t2","account_id":"angela","name":"Angela Cruz","grade":11,"subject":"Mathematics","topics":["Statistics"],"slots":["Thursday 4 PM","Wednesday 3 PM"],"eligible":True},
 {"id":"t3","account_id":"mark","name":"Mark Santos","grade":12,"subject":"Mathematics","topics":["Quadratic Equations"],"slots":["Wednesday 3 PM"],"eligible":True},
 {"id":"t4","account_id":"sofia","name":"Sofia Garcia","grade":11,"subject":"English","topics":["Grammar","Essay Writing"],"slots":["Wednesday 3 PM"],"eligible":True},
 {"id":"t5","account_id":"patricia","name":"Patricia Flores","grade":12,"subject":"English","topics":["Essay Writing"],"slots":["Friday 2 PM"],"eligible":True},
 {"id":"t6","account_id":"daniel","name":"Daniel Lim","grade":11,"subject":"Science","topics":["Biology"],"slots":["Monday 3 PM"],"eligible":True},
 {"id":"t7","account_id":"lea","name":"Lea Mendoza","grade":12,"subject":"Science","topics":["Chemistry"],"slots":["Thursday 4 PM"],"eligible":True},
 {"id":"t8","account_id":"carlo","name":"Carlo Navarro","grade":11,"subject":"Filipino","topics":["Panitikan"],"slots":["Friday 2 PM"],"eligible":True},
 {"id":"t9","account_id":"isabella","name":"Isabella Aquino","grade":12,"subject":"Filipino","topics":["Pagsulat"],"slots":["Wednesday 3 PM"],"eligible":True},
 {"id":"t10","name":"Nathan Bautista","grade":11,"subject":"Mathematics","topics":["Quadratic Equations"],"slots":["Wednesday 3 PM"],"eligible":False},
]
GROUPS = [
 {"id":"g1","name":"Math Study Circle","subject":"Mathematics","topic":"Quadratic Equations","slot":"Wednesday 3 PM","members":3,"capacity":5},
 {"id":"g2","name":"Algebra Buddies","subject":"Mathematics","topic":"Algebra","slot":"Friday 2 PM","members":2,"capacity":4},
 {"id":"g3","name":"Equation Explorers","subject":"Mathematics","topic":"Quadratic Equations","slot":"Friday 2 PM","members":6,"capacity":6},
 {"id":"g4","name":"English Review Club","subject":"English","topic":"Grammar","slot":"Wednesday 3 PM","members":2,"capacity":5},
 {"id":"g5","name":"Science Study Buddies","subject":"Science","topic":"Biology","slot":"Monday 3 PM","members":3,"capacity":5},
 {"id":"g6","name":"Panitikan Circle","subject":"Filipino","topic":"Panitikan","slot":"Friday 2 PM","members":2,"capacity":6},
]
