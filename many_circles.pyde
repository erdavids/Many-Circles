w, h = 1000, 1000

def circle1(x, y, r):
    
    max_section_length = r/30
    section_spacing = 5
    translate(x, y)
    strokeWeight(4)
    

    for i in range(360):
        rotate(radians(1))
        
        current_point = [0, 0]
        end_point = [0, current_point[1] + int(random(0, max_section_length))]
        while (end_point[1] + section_spacing < r/2):
            print(end_point[1]/(r/2))
        
            line(current_point[0], current_point[1], end_point[0], end_point[1])
            
            current_point = [0, end_point[1] + section_spacing]
            end_point = [0, current_point[1] + int(random(0, max_section_length))]
            
        
        line(current_point[0], current_point[1], current_point[0], r/2)
        

# Draw as many circle types as possible over time
def setup():
    size(w, h)
    background(255)
    pixelDensity(2)
    
    circle1(w/2, h/2, 750)
    
    
