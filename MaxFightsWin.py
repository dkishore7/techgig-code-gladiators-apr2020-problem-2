''' Read input from STDIN. Print your output to STDOUT '''
import bisect
from timeit import default_timer as timer

def win(list1, list2):
	sl1 = sorted(list1)
	sl2 = sorted(list2)

	list_1_min = min(sl1)
	list_1_max = max(sl1)

	list_2_min = min(sl2)    
	list_2_max = max(sl2)
    
#     Look for obvious comparisons
	if list_2_max < list_1_min:
		win_count = len(sl1)
    
	elif list_1_max <= list_2_min:
		win_count = 0
    
	else:
		win_count =0

		idx = 0
		list_1_slider = 0
		list_1_max_index = len(sl1) -1

		while (idx < len(sl2)) and (sl2[idx] < list_1_max) and (list_1_slider <= list_1_max_index):
			result = bisect.bisect_right(sl1,sl2[idx],lo=list_1_slider,hi=list_1_max_index)
			if result > list_1_max_index:
				print('breaking')
				break
			else: 
				win_count = win_count + 1
				idx = idx + 1
				list_1_slider = result + 1
	
	print(win_count)


def main():
    num_testcases = int(input())
    lines_to_read = 3*num_testcases
    input_list = []
    read_start = timer()
    
    for i in range(0,lines_to_read):
        input_list.append(input())
    read_end = timer()

    process_start = timer()        
    for j in range(0,num_testcases):
        list1 = list(map(int, input_list[1].split()))
        list2 = list(map(int, input_list[2].split()))
        del input_list[0:3]
        win(list1,list2)
    process_end = timer()
    
    print(f'Time Taken to Read lines: {read_end - read_start}')
    print(f'Time taken to process all testcases : {process_end - process_start}')
    print(f'Total Time Taken : {(read_end - read_start) + (process_end - process_start)}')

main()
