days_of_week = {
  1: 'Monday',
  2: 'Tuesday',
  3: 'Wednesday',
  4: 'Thursday',
  5: 'Friday',
  6: 'Saturday',
  7: 'Sunday'
}

user_input = input("Please enter days of week to remove. (i.e. enter \"12\" to remove Monday and Tuesday): ")
print('\n')

user_input1 = int(user_input[0])
user_input2 = int(user_input[1])

days_of_week.pop(user_input1)
days_of_week.pop(user_input2)

print(days_of_week, '\n')

personnel_list = {
  "John" : {
    "Age": 25,
    "Sex": "Male"
  },
  "Lisa": {
    "Age": 28,
    "Sex": "Female"
  }, 
  "Linda": {
    "Age": 32,
    "Sex": "Female"
  }, 
  "Michael": {
    "Age": 41,
    "Sex": "Male"
  }
  }
  
michael_children = {
  "michael_children" : {
  "Karen" : {
    "Age" : 12,
    "Sex": "Female"
  },
  "Greg": {
    "Age": 7,
    "Sex": "Male"
  }
}
}

linda_children = {
  "susan_children" : {
  "Susan": {
    "Age": 6,
    "Sex": "Female"
  }
}
}
personnel_list["Michael"].update(michael_children)
personnel_list["Linda"].update(linda_children)
print(personnel_list["Michael"]["michael_children"])

