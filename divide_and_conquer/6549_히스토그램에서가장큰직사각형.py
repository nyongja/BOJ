def hist_area(start, end, h) :
    if start == end :
        return h[start]
    else :
        mid  = (start + end) // 2
        # 중간을 기준으로 왼쪽, 오른쪽 각각 방향으로 체크
        cur_l = mid    # 현재 왼쪽 인덱스
        cur_r = mid + 1  # 현재 오른쪽 인덱스
        cur_h = min(h[cur_l], h[cur_r]) # 현재 높이
        tmp_area = cur_h * 2 # 경계선에 걸친 히스토그램 넓이
        
        cnt = 2
        while True :
            # 현재 왼쪽 인덱스가 가리키는 값이 0이거나 왼쪽이 끝 인덱스를 가리키고 있고
            # 오른쪽 인덱스가 가리키는 값이 0이거나 오른쪽 끝 인덱스를 가리키고 있으면 더 이상 볼 게 없으므로 break
            if (h[cur_l] == 0 or cur_l == start) and (h[cur_r] == 0 or cur_r == end) :
                break
            # 왼쪽 인덱스만 0 또는 왼쪽이 끝 인덱스라면
            # 아직 오른쪽은 더 살펴볼 수 있음
            elif h[cur_l] == 0 or cur_l == start : 
                if h[cur_r + 1] < cur_h : # 오른쪽 인덱스가 가리키는 히스토그램이 현재 높이보다 낮으면
                    cur_h = h[cur_r + 1] # 낮은 높이 저장 (해당 높이까지 넓이 계산해야하므로)
                cur_r += 1
            # 오른쪽 인덱스만 0 또는 오른쪽이 끝 인덱스라면
            # 왼쪽은 더 살펴볼 수 있음
            elif h[cur_r] == 0 or cur_r == end :
                if h[cur_l - 1] < cur_h : # 왼쪽 인덱스가 가리키는 히스토그램이 현재 높이보다 낮으면
                    cur_h = h[cur_l - 1] # 낮은 높이 저장 (해당 높이까지 넓이 계산해야하므로)
                cur_l -= 1
            # 양쪽을 다 살펴볼 수 있는 경우라면
            else : # 더 높은쪽을 먼저 살펴봐야 최대한 넓은 히스토그램을 살펴 볼 수 있음
                if h[cur_l - 1] > h[cur_r + 1] : # 왼쪽 높이가 더 높은 경우에
                    if h[cur_l - 1] < cur_h :
                        cur_h = h[cur_l - 1]
                    cur_l -= 1
                else : # 오른쪽 히스토그램 높이가 더 높은 경우
                    if h[cur_r + 1] < cur_h :
                        cur_h = h[cur_r + 1]
                    cur_r += 1
            cnt += 1
            tmp_area = max(tmp_area, cur_h * cnt)
        return max(hist_area(start, mid, heights), hist_area(mid+1, end, heights), tmp_area)

n, *heights = list(map(int, input().split()))
while n != 0 :
    print(hist_area(0, len(heights)-1, heights))
    n, *heights = list(map(int, input().split())) # 다음 input