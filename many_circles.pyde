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
        
# Create a base deformed circle and then iterate off of it    
def circle_eight(x, y, r):
    translate(x, y)
    noFill()
    strokeWeight(4)
    
    points = []
    for i in range(0, 360, 15):
        points.append((r/2*sin(radians(i)), r/2*cos(radians(i))))
    
    # Create the base
    final = []
    for p in points:
        x_change = p[0] / 55.0
        y_change = p[1] / 55.0
        
        change = random(-3, 3)
        p = (p[0] + x_change * change, p[1] + y_change * change)
        final.append(p)


    for i in range(8):
        variation = []
        for p in final:
            x_change = p[0] / 55.0
            y_change = p[1] / 55.0
            
            change = random(-2, 2)
            p = (p[0] + x_change * change, p[1] + y_change * change)
            variation.append(p)
        
        beginShape()
        for p in variation:
            curveVertex(*p)
        curveVertex(*variation[0])
        curveVertex(*variation[1])
        curveVertex(*variation[2])
        endShape()
        
        
def draw_line(p, v, l, d, md, r):
    if (d > md):
        return
    
    
    
    start_point = p[:]
    end_point = (p[0] + v[0] * l, p[1] + v[1] * l)
    
    if (distance(end_point, (0, 0)) > r/2):
        draw_line(start_point, v, l*.3, d, md, r)

    
        
    if (distance(end_point, (0, 0)) > r/2):
        return
    
    #line(start_point[0], start_point[1], end_point[0], end_point[1])
    strokeWeight(2)
    lr = -40
    hr = 40
    curve(start_point[0] + random(lr, hr), start_point[1] + random(lr, hr), start_point[0], start_point[1], end_point[0], end_point[1], end_point[0] + random(lr, hr), end_point[1] + random(lr, hr))
    
    if (random(1) < 1):
        v_one = v.copy()
        v_one.rotate(random(0, .16) * PI)
        draw_line(end_point, v_one, l, d + 1, md, r)
    
    if (random(1) < 1):
        v_two = v.copy()
        v_two.rotate(random(1.84, 2) * PI)
        draw_line(end_point, v_two, l, d + 1, md,r )
    
def circle_nine(x, y, r):
    translate(x, y)

    noFill()
    strokeWeight(4)
    

    
    for i in range(8):
        rotate(radians(i * 45))
        draw_line((0, 0), PVector(2, 2), 12, 1, 12, r)
    

def circle_ten(x, y, r):
    
    translate(x, y)
    noFill()
    
    strokeCap(ROUND)
    strokeWeight(4)
        
    count = 60
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), (r/2 - j*r/2/count)*cos(radians(i))))
            
        beginShape()
        for p in points:
            curveVertex(*p)
            if (random(1) < .1):
                endShape()
                beginShape()
        curveVertex(*points[0])
        curveVertex(*points[1])
        curveVertex(*points[2])
        endShape()

def circle_eleven(x, y, r):
    translate(x, y)
    noFill()
    
    strokeCap(ROUND)
    strokeWeight(4)
        
    count = 60
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), r/2*cos(radians(i))))
            
        beginShape()
        for p in points:
            curveVertex(*p)
            if (random(1) < .1):
                endShape()
                beginShape()
        curveVertex(*points[0])
        curveVertex(*points[1])
        curveVertex(*points[2])
        endShape()
        
    stroke(255)
    strokeWeight(20)
    circle(0, 0, r+20)
    
def circle_twelve(x, y, r):
    translate(x, y)
    noFill()
    
    strokeCap(ROUND)
    strokeWeight(4)
        
    count = 60
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), r/2*cos(radians(i))))
            
        beginShape()
        for p in points:
            curveVertex(*p)
            if (random(1) < .1):
                endShape()
                beginShape()
        curveVertex(*points[0])
        curveVertex(*points[1])
        curveVertex(*points[2])
        endShape()
        
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append((r/2*sin(radians(i)), (r/2 - j*r/2/count)*cos(radians(i))))
            
        beginShape()
        for p in points:
            curveVertex(*p)
            if (random(1) < .1):
                endShape()
                beginShape()
        curveVertex(*points[0])
        curveVertex(*points[1])
        curveVertex(*points[2])
        endShape()
        
    stroke(255)
    strokeWeight(20)
    circle(0, 0, r+20)
    
    

# Simple Circle Packing with 250000 circles
# Takes a long time with the brute force method, not really worth optimizing for this project though
def circle_thirteen(x, y, r):
    translate(x, y)
    strokeWeight(2)
    points = []
    for j in range(25000):
        new_p = ((random(-r/2, r/2), random(-r/2, r/2)))
        
        valid = True
        if distance(new_p, (0, 0)) < r/2:
            for p in points:
                if (distance(new_p, p) < 3):
                    valid = False
            if valid:
                point(*new_p)
                points.append(new_p)

# Circle packing with a relaxed distance requirement further from center
# Not sure if I will keep this one
def circle_fourteen(x, y, r):
    translate(x, y)
    strokeWeight(2)
    points = []
    for j in range(25000):
        new_p = ((random(-r/2, r/2), random(-r/2, r/2)))
        
        valid = True
        if distance(new_p, (0, 0)) < r/2:
            for p in points:
                if (distance(new_p, p) < 10 - distance(p, (0,0))/float(r/2) * 10):
                    valid = False
            if valid:
                point(*new_p)
                points.append(new_p)
                
                
def circle_fifteen(x, y, r):
    translate(x, y)
    noFill()
    
    strokeCap(ROUND)
    strokeWeight(1)
        
    count = 50
    for j in range(count):
        points = []
        for i in range(0, 360, 2):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), (r/2 - j*r/2/count)*cos(radians(i))))
            
        beginShape()
        for p in points:
            if (random(1) < .6):
                circle(p[0], p[1], 3)
                
def circle_sixteen(x, y, r):
    translate(x, y)
    noFill()
    
    strokeCap(ROUND)
    strokeWeight(1)
        
    count = 20
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), (r/2 - j*r/2/count)*cos(radians(i))))
            
        beginShape()
        for p in points:
            if (random(1) < .6):
                line(p[0], p[1], p[0] + random(-3, 3), p[1] + random(-3, 3))
                
                
def circle_seventeen(x, y, r):
    translate(x, y)
    noFill()
    
    strokeCap(ROUND)
    strokeWeight(1)
        
    count = 20
    for j in range(count):
        points = []
        for i in range(0, 360, 1):
            points.append(((r/2 - j*r/2/count)*sin(radians(i)), (r/2 - j*r/2/count)*cos(radians(i))))
            
        beginShape()
        for p in points:
            if (random(1) < .6):
                line(p[0], p[1], p[0] + random(-3, 3), p[1] + random(-3, 3))

##################
#
# Helper functions
#
##################

def draw_random_points_between(p1, p2, n, d):
    for i in range(n):
        u = random(1)
        
        x_dev = random(-d, d)
        y_dev = random(-d, d)
        
        point((1 - u)*p1[0] + u * p2[0] + x_dev, (1 - u)*p1[1] + u * p2[1] + y_dev)

    
# Used by: Many:
def distance(p1, p2):
    return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

# Draw as many circle types as possible over time
def setup():
    size(w, h)
    background(255)
    pixelDensity(2)
    
    circle_seventeen(w/2, h/2, 750)
    
    save("Circles/circle_seventeen.png")
    
    
