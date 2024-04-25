def group_time_slots(time_list):
    grouped_times = []
    temp_group = []
    for time_slot in time_list:
        temp_group.append(time_slot)
        if len(temp_group) == 4:
            grouped_times.append(temp_group)
            temp_group = []
    if temp_group:
        grouped_times.append(temp_group)
    return grouped_times

time_all = [
    '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
    '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
    '18:00', '18:30', '19:00'
]

time_group = group_time_slots(time_all)
print(time_group)