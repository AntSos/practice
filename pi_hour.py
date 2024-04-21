#PythonInstitute exercises for undertand the use of // and % operators

def time_c (hour, mins, t_event):
    
    w_time = (hour*60) + (mins) + t_event
    t_e_hour = w_time // 60
    t_e_mins = w_time % 60

    print (f"It ends at: {t_e_hour}:{t_e_mins}")

def main ():
    hour = int(input ("Hour starting event: "))
    mins = int(input ("Minutes starting event: "))
    t_event = int(input ("Event duration in minutes: "))
    print (time_c (hour, mins, t_event))

if __name__ == "__main__":
    main ()