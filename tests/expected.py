"""Expected test results"""
TEST_1 = """[\
{\
"category": "Local Eats", \
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}, {"name": "Smitty's Family Restaurant (St. James)", "address": \
"1017 St James St, Winnipeg, MB R3H 0K6"}, {"name": "Food Trip Kitchen", "address": "1045 St \
James Street, Winnipeg, Manitoba R3H 0K6"}, {"name": "Vi-Ann Restaurant", "address": "1020 \
Notre Dame Ave, Winnipeg, Manitoba R3E0N5"}, {"name": "Burrito Splendido (1046 henderson-)", \
"address": "1046 Henderson Highway, Winnipeg, NAMER R2K 2M5"}, {"name": "Panda Tea (McPhillips \
St)", "address": "1041 Mcphillips St, Winnipeg, MB R2X 2K6"}, {"name": "Smitty's Family \
Restaurant (Henderson)", "address": "#9 1919 Henderson Highway, Winnipeg, MB R2G 1P4"}] \
}, \
{ \
"category": "American", \
"venues": [{"name": "Smitty's Family Restaurant (St. James)", "address": "1017 St \
James St, Winnipeg, MB R3H 0K6"}, {"name": "McDonald's (1001 Empress Street)", "address": "1001 \
Empress Street, Winnipeg, MB R3R 3P8"}, {"name": "Smitty's Family Restaurant (Henderson)", \
"address": "#9 1919 Henderson Highway, Winnipeg, MB R2G 1P4"}, {"name": "Burger King #7961 (100 \
21st Street North)", "address": "100 21st Street North, Moorhead, MN 56560"}] \
}, \
{ \
"category": "Asian",
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}, {"name": "Vi-Ann Restaurant", "address": "1020 Notre Dame Ave, \
Winnipeg, Manitoba R3E0N5"}, {"name": "Panda Tea (McPhillips St)", "address": "1041 Mcphillips \
St, Winnipeg, MB R2X 2K6"}] \
}, \
{ \
"category": "Fast Food", \
"venues": [{"name": "McDonald's (1001 Empress Street)", "address": "1001 Empress \
Street, Winnipeg, MB R3R 3P8"}, {"name": "Little Caesars (Henderson Hwy)", "address": "1050 \
Henderson Hwy, Winnipeg, MB R3K 2M5"}, {"name": "Burger King #7961 (100 21st Street North)", \
"address": "100 21st Street North, Moorhead, MN 56560"}] \
}, \
{ \
"category": "Breakfast and Brunch", \
"venues": [{"name": "Smitty's Family Restaurant (St. James)", "address": "1017 St \
James St, Winnipeg, MB R3H 0K6"}, {"name": "Smitty's Family Restaurant (Henderson)", "address": \
"#9 1919 Henderson Highway, Winnipeg, MB R2G 1P4"}] \
}, \
{ \
"category": "Burgers", \
"venues": [{"name": "McDonald's (1001 Empress Street)", "address": "1001 Empress \
Street, Winnipeg, MB R3R 3P8"}, {"name": "Smitty's Family Restaurant (Henderson)", "address": \
"#9 1919 Henderson Highway, Winnipeg, MB R2G 1P4"}] \
}, \
{ \
"category": "Chicken", \
"venues": [{"name": "Food Trip Kitchen", "address": "1045 St James Street, \
Winnipeg, Manitoba R3H 0K6"}, {"name": "Smitty's Family Restaurant (Henderson)", "address": "#9 \
1919 Henderson Highway, Winnipeg, MB R2G 1P4"}] \
}, \
{ \
"category": "Sandwiches", \
"venues": [{"name": "Smitty's Family Restaurant (St. James)", "address": "1017 St \
James St, Winnipeg, MB R3H 0K6"}, {"name": "Smitty's Family Restaurant (Henderson)", "address": \
"#9 1919 Henderson Highway, Winnipeg, MB R2G 1P4"}] \
}, \
{ \
"category": "Allergy Friendly", \
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}] \
}, \
{ \
"category": "Asian Fusion", \
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}] \
}, \
{ \
"category": "burger", \
"venues": [{"name": "Burger King #7961 (100 21st Street North)", "address": "100 \
21st Street North, Moorhead, MN 56560"}] \
}, \
{ \
"category": "Chinese", \
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}] \
}, \
{ \
"category": "Desserts", \
"venues": [{"name": "Panda Tea (McPhillips St)", "address": "1041 Mcphillips St, \
Winnipeg, MB R2X 2K6"}] \
}, \
{ \
"category": "Family Meals", \
"venues": [{"name": "Burger King #7961 (100 21st Street North)", "address": "100 \
21st Street North, Moorhead, MN 56560"}] \
}, \
{ \
"category": "Filipino", \
"venues": [{"name": "Food Trip Kitchen", "address": "1045 St James Street, \
Winnipeg, Manitoba R3H 0K6"}] \
}, \
{ \
"category": "Fish and Chips", \
"venues": [{"name": "Smitty's Family Restaurant (Henderson)", "address": "#9 1919 \
Henderson Highway, Winnipeg, MB R2G 1P4"}] \
}, \
{ \
"category": "Healthy", \
"venues": [{"name": "Smitty's Family Restaurant (Henderson)", "address": "#9 1919 \
Henderson Highway, Winnipeg, MB R2G 1P4"}] \
}, \
{ \
"category": "Juice and Smoothies", \
"venues": [{"name": "Panda Tea (McPhillips St)", "address": "1041 Mcphillips St, \
Winnipeg, MB R2X 2K6"}] \
}, \
{ \
"category": "Latin American", \
"venues": [{"name": "Burrito Splendido (1046 henderson-)", "address": "1046 \
Henderson Highway, Winnipeg, NAMER R2K 2M5"}] \
}, \
{ \
"category": "New Mexican", \
"venues": [{"name": "Burrito Splendido (1046 henderson-)", "address": "1046 \
Henderson Highway, Winnipeg, NAMER R2K 2M5"}] \
}, \
{ \
"category": "Noodles", \
"venues": [{"name": "Vi-Ann Restaurant", "address": "1020 Notre Dame Ave, Winnipeg, \
Manitoba R3E0N5"}] \
}, \
{ \
"category": "Pizza", \
"venues": [{"name": "Little Caesars (Henderson Hwy)", "address": "1050 Henderson \
Hwy, Winnipeg, MB R3K 2M5"}] \
}, \
{ \
"category": "Salads", \
"venues": [{"name": "Smitty's Family Restaurant (Henderson)", "address": "#9 1919 \
Henderson Highway, Winnipeg, MB R2G 1P4"}] \
}, \
{ \
"category": "Seafood", \
"venues": [{"name": "Food Trip Kitchen", "address": "1045 St James Street, \
Winnipeg, Manitoba R3H 0K6"}] \
}, \
{ \
"category": "South East Asian", \
"venues": [{"name": "Food Trip Kitchen", "address": "1045 St James Street, \
Winnipeg, Manitoba R3H 0K6"}] \
}, \
{ \
"category": "Thai", \
"venues": [{"name": "Vi-Ann Restaurant", "address": "1020 Notre Dame Ave, Winnipeg, \
Manitoba R3E0N5"}] \
} \
]"""

TEST_2 = """[\
{\
"category": "Local Eats",\
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}, {"name": "Smitty's Family Restaurant (St. James)", "address":\
"1017 St James St, Winnipeg, MB R3H 0K6"}, {"name": "Food Trip Kitchen", "address": "1045 St \
James Street, Winnipeg, Manitoba R3H 0K6"}]\
},\
{\
"category": "Allergy Friendly",\
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina Hwy, \
Winnipeg, MB R3T 2G6"}]\
},\
{\
"category": "American",\
"venues": [{"name": "Smitty's Family Restaurant (St. James)", "address": "1017 St \
James St, Winnipeg, MB R3H 0K6"}]\
},\
{\
"category": "Asian",\
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}]\
},\
{\
"category": "Asian Fusion",\
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}]\
},\
{\
"category": "Breakfast and Brunch",\
"venues": [{"name": "Smitty's Family Restaurant (St. James)", "address": "1017 St \
James St, Winnipeg, MB R3H 0K6"}]\
},\
{\
"category": "Chicken",\
"venues": [{"name": "Food Trip Kitchen", "address": "1045 St James Street, \
Winnipeg, Manitoba R3H 0K6"}]\
},\
{\
"category": "Chinese",\
"venues": [{"name": "Dagu Rice Noodle (Winnipeg)", "address": "102-1855 Pembina \
Hwy, Winnipeg, MB R3T 2G6"}]\
},\
{\
"category": "Filipino",\
"venues": [{"name": "Food Trip Kitchen", "address": "1045 St James Street, \
Winnipeg, Manitoba R3H 0K6"}]\
},\
{\
"category": "Sandwiches",\
"venues": [{"name": "Smitty's Family Restaurant (St. James)", "address": "1017 St \
James St, Winnipeg, MB R3H 0K6"}]\
},\
{\
"category": "Seafood", \
"venues": [{"name": "Food Trip Kitchen", "address": "1045 St James Street, \
Winnipeg, Manitoba R3H 0K6"}]\
},\
{\
"category": "South East Asian", \
"venues": [{"name": "Food Trip Kitchen", "address": "1045 St James Street, \
Winnipeg, Manitoba R3H 0K6"}]\
}\
]"""