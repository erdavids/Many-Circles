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
    
# Domain Warping Circle (Cool effect but not super practical for multiple circles)
def circle_four(x, y, r):
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
    
    stroke(col)
    
# Used by: Circle 4:
def distance(p1, p2):
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

# Draw as many circle types as possible over time
def setup():
    size(w, h)
    background(255)
    pixelDensity(2)
    
    circle_four(w/2, h/2, 750)
    
    save("Circles/circle_four.png")
    
    
