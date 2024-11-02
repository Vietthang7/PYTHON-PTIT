def triangle_area(x1, y1, x2, y2, x3, y3):  
    """ Tính diện tích của tam giác bằng công thức. """  
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)  

def is_point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):  
    """ Kiểm tra xem điểm (px, py) có nằm trong tam giác hay không. """  
    A = triangle_area(x1, y1, x2, y2, x3, y3)  
    A1 = triangle_area(px, py, x2, y2, x3, y3)  
    A2 = triangle_area(x1, y1, px, py, x3, y3)  
    A3 = triangle_area(x1, y1, x2, y2, px, py)  
    return A == A1 + A2 + A3  

def main():  
    N = int(input())  
    triangles = []  

    for _ in range(N):  
        triangle = list(map(int, input().split()))  
        triangles.append(triangle)  

    # Sử dụng một tập hợp để lưu các điểm bị che phủ  
    covered_points = set()  

    # Duyệt qua từng tam giác  
    for x1, y1, x2, y2, x3, y3 in triangles:  
        # Tìm biên giới của tam giác  
        min_x = min(x1, x2, x3)  
        max_x = max(x1, x2, x3)  
        min_y = min(y1, y2, y3)  
        max_y = max(y1, y2, y3)  

        # Duyệt qua tất cả các điểm trong hình chữ nhật bao quanh tam giác  
        for x in range(min_x, max_x + 1):  
            for y in range(min_y, max_y + 1):  
                # Nếu điểm (x, y) nằm trong tam giác, thì đánh dấu nó  
                if is_point_in_triangle(x, y, x1, y1, x2, y2, x3, y3):  
                    covered_points.add((x, y))  

    # In ra diện tích che phủ  
    print(f"{len(covered_points):.6f}")  

if __name__ == "__main__":  
    main()