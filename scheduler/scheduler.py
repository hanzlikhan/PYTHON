import matplotlib.pyplot as plt
import random

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival_time'])
    
    current_time = 0
    gantt_chart = []
    waiting_times = []
    turnaround_times = []

    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']
        
        start_time = current_time
        end_time = start_time + process['burst_time']

        gantt_chart.append((process['pid'], start_time, end_time))

        turnaround_time = end_time - process['arrival_time']
        turnaround_times.append(turnaround_time)

        waiting_time = turnaround_time - process['burst_time']
        waiting_times.append(waiting_time)

        current_time = end_time

    return gantt_chart, waiting_times, turnaround_times

def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x['arrival_time'], x['burst_time']))
    
    current_time = 0
    gantt_chart = []
    waiting_times = []
    turnaround_times = []
    remaining_processes = processes[:]

    while remaining_processes:
        available_processes = [p for p in remaining_processes if p['arrival_time'] <= current_time]
        if not available_processes:
            current_time = remaining_processes[0]['arrival_time']
            continue

        process = min(available_processes, key=lambda x: x['burst_time'])
        remaining_processes.remove(process)

        start_time = current_time
        end_time = start_time + process['burst_time']

        gantt_chart.append((process['pid'], start_time, end_time))

        turnaround_time = end_time - process['arrival_time']
        turnaround_times.append(turnaround_time)

        waiting_time = turnaround_time - process['burst_time']
        waiting_times.append(waiting_time)

        current_time = end_time

    return gantt_chart, waiting_times, turnaround_times

def round_robin_scheduling(processes, time_quantum):
    queue = processes[:]
    current_time = 0
    gantt_chart = []
    waiting_times = {p['pid']: 0 for p in processes}
    turnaround_times = {p['pid']: 0 for p in processes}

    remaining_burst_times = {p['pid']: p['burst_time'] for p in processes}

    while queue:
        process = queue.pop(0)

        if current_time < process['arrival_time']:
            current_time = process['arrival_time']

        execute_time = min(remaining_burst_times[process['pid']], time_quantum)
        start_time = current_time
        end_time = start_time + execute_time

        gantt_chart.append((process['pid'], start_time, end_time))
        current_time = end_time

        remaining_burst_times[process['pid']] -= execute_time

        if remaining_burst_times[process['pid']] > 0:
            queue.append(process)
        else:
            turnaround_times[process['pid']] = current_time - process['arrival_time']

        waiting_times[process['pid']] = turnaround_times[process['pid']] - process['burst_time']

    return gantt_chart, list(waiting_times.values()), list(turnaround_times.values())

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x['arrival_time'], x['priority']))

    current_time = 0
    gantt_chart = []
    waiting_times = []
    turnaround_times = []
    remaining_processes = processes[:]

    while remaining_processes:
        available_processes = [p for p in remaining_processes if p['arrival_time'] <= current_time]
        if not available_processes:
            current_time = remaining_processes[0]['arrival_time']
            continue

        process = min(available_processes, key=lambda x: x['priority'])
        remaining_processes.remove(process)

        start_time = current_time
        end_time = start_time + process['burst_time']

        gantt_chart.append((process['pid'], start_time, end_time))

        turnaround_time = end_time - process['arrival_time']
        turnaround_times.append(turnaround_time)

        waiting_time = turnaround_time - process['burst_time']
        waiting_times.append(waiting_time)

        current_time = end_time

    return gantt_chart, waiting_times, turnaround_times

def display_gantt_chart(gantt_chart):
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"P{entry[0]}: [{entry[1]}-{entry[2]}]", end=" ")
    print()

    fig, ax = plt.subplots()
    colors = plt.cm.tab10.colors

    for entry in gantt_chart:
        process_id = entry[0]
        color = colors[(process_id - 1) % len(colors)]
        ax.broken_barh([(entry[1], entry[2] - entry[1])], (10, 9), facecolors=color, label=f"P{process_id}")

    handles, labels = ax.get_legend_handles_labels()
    unique_labels = dict(zip(labels, handles))  # Remove duplicates
    ax.legend(unique_labels.values(), unique_labels.keys(), loc='upper right')

    ax.set_xlabel("Time")
    ax.set_yticks([15])
    ax.set_yticklabels(['Processes'])
    ax.grid(True)
    plt.show()

def calculate_averages(waiting_times, turnaround_times):
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    return avg_waiting_time, avg_turnaround_time

def main():
    print("Scheduling Methods:")
    print("1. First Come First Serve (FCFS)")
    print("2. Shortest Job First (SJF)")
    print("3. Round Robin (RR)")
    print("4. Priority Scheduling")
    choice = int(input("\nSelect a scheduling method (1-4): "))

    n = int(input("\nEnter the number of processes: "))
    processes = []

    for i in range(n):
        arrival_time = int(input(f"Enter arrival time for process P{i+1}: "))
        burst_time = int(input(f"Enter burst time for process P{i+1}: "))
        if choice == 4:
            priority = int(input(f"Enter priority for process P{i+1} (lower number = higher priority): "))
            processes.append({"pid": i + 1, "arrival_time": arrival_time, "burst_time": burst_time, "priority": priority})
        else:
            processes.append({"pid": i + 1, "arrival_time": arrival_time, "burst_time": burst_time})

    if choice == 1:
        gantt_chart, waiting_times, turnaround_times = fcfs_scheduling(processes)
    elif choice == 2:
        gantt_chart, waiting_times, turnaround_times = sjf_scheduling(processes)
    elif choice == 3:
        time_quantum = int(input("Enter time quantum for Round Robin: "))
        gantt_chart, waiting_times, turnaround_times = round_robin_scheduling(processes, time_quantum)
    elif choice == 4:
        gantt_chart, waiting_times, turnaround_times = priority_scheduling(processes)
    else:
        print("Invalid choice.")
        return

    display_gantt_chart(gantt_chart)

    avg_waiting_time, avg_turnaround_time = calculate_averages(waiting_times, turnaround_times)
    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

if __name__ == "__main__":
    main()
