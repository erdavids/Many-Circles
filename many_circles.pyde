w, h = 1000, 1000

# Rotate around the center and draw spaced out line sections to the edges
def circle_one(x, y, r):
    
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
        
# Create inner circles that intersect perfectly with the edge
def circle_two(x, y, r):
    circle_count = 1500
    
    pushMatrix()
    translate(x, y)
    circle(0, 0, r)
    noFill()
    for i in range(circle_count):
        rotate(random(2*PI))
        cent = int(random(0, r/2))

        circle(0, cent, r - (cent * 2))
        
        
    popMatrix()
    
# Similar to circle_two, just a different circle calculation/count
def circle_three(x, y, r):
    circle_count = 100
    
    pushMatrix()
    translate(x, y)
    circle(0, 0, r)
    noFill()
    for i in range(circle_count):
        rotate(random(2*PI))
        cent = int(random(0, r/10))

        circle(0, cent, r - (cent * 2))
        
        
    popMatrix()
    
# Pure Random Walk (added parameter for depth in case of recursion)
def circle_four(x, y, r, d):
    pushMatrix()
    translate(x, y)
    noFill()
    stroke(0, 20)
    
    steps = [-1, 1]
    rotate(random(2*PI))
    current_point = [0, r/2.2]
    if (d < 50):
        while(distance(current_point, (0, 0)) < r/2):
            point(current_point[0], current_point[1])
        
            current_point[0] += random(-1, 1)
            current_point[1] += random(-1, 1)
    else:
        return
    
    popMatrix()
    circle_four(x, y, r, d + 1)
    
    
# Directed random walk
def circle_five(x, y, r, d):
    pushMatrix()
    translate(x, y)
    noFill()
    stroke(0, 255)
    
    steps = [-4, 4, 0, 0]
    rotate(random(2*PI))
    current_point = [0, 0]
    if (d < 100):
        while(distance(current_point, (0, 0)) < r/2):
            point(current_point[0], current_point[1])
        
            current_point[0] += steps[int(random(len(steps)))]
            if (current_point[0] != 0):
                current_point[1] += steps[int(random(len(steps) - 2))]
    else:
        return
    
    popMatrix()
    circle_five(x, y, r, d + 1)
    
# Directed random walk with lines
def circle_six(x, y, r, d):
    pushMatrix()
    translate(x, y)
    noFill()
    stroke(0, 255)
    
    steps = [-7, 7, 0, 0]
    rotate(random(2*PI))
    current_point = [0, 0]
    last_point = current_point[:]
    if (d < 100):
        while(distance(current_point, (0, 0)) < r/2):
            current_point[0] += steps[int(random(len(steps)))]
            if (current_point[0] != 0):
                current_point[1] += steps[int(random(len(steps) - 2))]
                
            line(current_point[0], current_point[1], last_point[0], last_point[1])
            
            last_point = current_point[:]
    else:
        return
    
    popMatrix()
    circle_six(x, y, r, d + 1)
    
def circle_seven(x, y, r):
    translate(x, y)
    noFill()

    arc_count = 200
        
    for i in range(arc_count):
        strokeWeight(random(2, 3))
        rotate(random(2*PI))
        a = random(r)
        arc(0, 0, a, a, 0, PI)
        
        
            
    

# Domain Warping Circle (Cool effect but not super practical for multiple circles)
# Might move this lower down (Doesn't fully fit the style of the other circles)
def circle_something(x, y, r):
    translate(x, y)
    noFill()
    stroke(0)
    
    noise_scale = .02
    
    strokeWeight(2)    
    circle(0, 0, r)
    
    for i in range(-r/2, r/2):
        for j in range(-r/2, r/2):
            if (distance((j, i), (0, 0)) < r/2):
                warp(j * noise_scale, i * noise_scale)
                
                point(j, i)
                
            
            
##################
#
# Helper functions
#
##################

# Used by: Circle 4, 
def fbm(x, y):
    return noise(x, y)

# Used by: Circle 4,
# f(p) = fbm(p + fbm(p + fbm(p)))
def warp(x, y):
    
    q = (fbm(x + 1, y + 1), fbm(x + 2, y + 2))
    r = (fbm(x + 4.0 * q[0], y + 4.0 * q[1]), fbm(x + 4.0 * q[0] + 1, y + 4.0 * q[1] + 1))
    
    
    c = fbm(x + 4.0 * r[0], y + 4.0 * r[1])
    col = 255.0 * c
    
    stroke(col, 255)
    
# Used by: Many:
def distance(p1, p2):
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

# Draw as many circle types as possible over time
def setup():
    size(w, h)
    background(255)
    pixelDensity(2)
    
    circle_eight(w/2, h/2, 750)
    
    save("Circles/circle_eight.png")
    
    
