logs = [
    ("2026-06-19 10:00", "INFO", "Model Loaded"),
    ("2026-06-19 10:05", "ERROR", "API Timeout"),
    ("2026-06-19 10:08", "WARNING", "High Memory"),
    ("2026-06-19 10:10", "INFO", "Prediction Completed"),
    ("2026-06-19 10:12", "ERROR", "API Timeout"),
    ("2026-06-19 10:15", "INFO", "Prediction Completed"),
    ("2026-06-19 10:18", "ERROR", "Database Connection Failed"),
    ("2026-06-19 10:20", "WARNING", "Disk Usage High"),
    ("2026-06-19 10:25", "INFO", "Model Reloaded"),
    ("2026-06-19 10:30", "ERROR", "API Timeout")
]

# ===============================================================================

# Problem - 1

# 1) Store all ERROR log messages in a new list.

# new_list=[]
# for details in logs:
#     if details[1]=="ERROR":
#         new_list.append(details)
# print(new_list)


# 2) Store all timestamps of WARNING logs.

# new_list=[]
# for details in logs:
#     if details[1]=="WARNING":
#         new_list.append(details[0])
# print(new_list)

#===============================================================================

# Problem-2

# 1) Print each log using tuple unpacking.

# for details in logs:
#     time_stamps , info , data = details
#     print(time_stamps , info , data)


# 2) Create a tuple containing only (Timestamp, Message) for every ERROR log.

# tup=()
# for details in logs:
#     tup+=((details[0],details[2]),)
# print(tup)

# 2a)

# lst = []
# for deatils in logs:
#     lst.append([deatils[0],details[2]])
# print(lst)

#===============================================================================

# Problem-3

# 1) Find all unique log levels.

# ans=[]
# seen=set()
# for details in logs:
#     if details[1] not in seen:
#         ans.append(details[1])
#     seen.add(details[1])
# print(ans) 


# 2) Find unique error messages.

# ans=[]
# seen=set()
# for details in logs:
#     if details[1]=="ERROR" and details[2] not in seen:
#             ans.append(details[2])
#     seen.add(details[2])
# print(ans) 

#===============================================================================

# Problem-4

# 1) Count the number of logs for each level.

# counts = []
# for details in logs:
#     level = details[1]
#     for i, (lvl, count) in enumerate(counts):
#         if lvl == level:
#             counts[i] = (lvl, count + 1)
#             break
#     else:
#         counts.append((level, 1))
# print(counts)

# 2) Count each error message.

# d={}
# for details in logs:
#     if details[1]=="ERROR" and details[2] in d:
#         d[details[2]]+=1
#     elif details[1]=="ERROR" and details[2] not in d:
#         d[details[2]]=1

# print(d)

#===============================================================================

# Problem-5

# 1) Extract all INFO messages.

# for details in logs:
#     if details[1]=="INFO":
#         print(details[2])

# 2) Extract all timestamps.

# for details in logs:
#         print(details[0])

#===============================================================================

# Problem-6

# Create a dictionary with log level as key and count as value.
    
# d={}
# for details in logs:
#     if details[1] in d:
#         d[details[1]]+=1
#     else:
#         d[details[1]]=1
# print(d)


#===============================================================================

# Problem-7

# 1) Convert all log messages to uppercase.

# lst=[]
# for deatils in logs:
#     d = list(deatils)
#     d[2]=d[2].upper()
#     lst.append((d[0],d[1],d[2]))
# print(lst)

# 1a)

# lst = [
#     (timestamp, level, message.upper())
#     for timestamp, level, message in logs
# ]

# print(lst)


# 2) Extract only the date from each timestamp.

# for deatils in logs:
#     date_time = deatils[0].split()
#     date = date_time[0]
#     print(date)


#===============================================================================  
          
# Problem - 8

# 1) Filter only ERROR logs.

# print(list(filter(lambda details : details[1]=="ERROR" , logs)))


# 2) Filter logs whose message contains the word "Model".

# print(list(filter(lambda deatils : deatils[2].startswith("Model"),logs)))

#===============================================================================  


# Problem-9

# 1) Given:
        # timestamps = [...]
        # levels = [...]
        # messages = [...]
# Combine them into a list of tuples.

# lst=[]
# timestamps = [details[0] for details in logs]
# levels = [details[1] for details in logs]
# messages = [details[2] for details in logs]

# for time_stamp , level , message in zip(timestamps, levels ,messages):
#         lst.append((time_stamp , level , message))
# print(lst)


# 2) Create a dictionary mapping timestamp to message.

# d={}
# for timestamp,message in zip(timestamps,messages):
#         d[timestamp] = message
# print(d)


#=============================================================================== 

# Problem -10

# 1) Print log number before each log.

# for i in range(len(logs)):
#     details = logs[i]
#     print(f"{i+1}.{details}")

# 2) Create a dictionary where key is log number and value is the log tuple.

# d={}
# for i in range(len(logs)):
#     details = logs[i]
#     d[i+1]=details
# print(d)

#=============================================================================== 

# Problem - 11
# 1) Create a generator that yields one ERROR log at a time.


# gen =  (details for details in logs if details[1]=="ERROR" )

# for i in gen:
#     print(i)

# 1a)
# def gen_func():
#     for details in logs:
#         if details[1]=="ERROR":
#             yield details
# errors = gen_func()
# for i in errors:
#     print(i)
    

# 2) Create a generator that yields one log record at a time.

# gen =  (details for details in logs)
# for i in gen:
#     print(i)


#=============================================================================== 




