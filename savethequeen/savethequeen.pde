PImage bg;
Quiz q;
Ufo u;

void setup() {
  size(640, 480);
  frameRate(60);
  bg = loadImage("img/background.png");
  q = new Quiz();
  u = new Ufo("img/ufo/ufo_", 12);  
}

void draw() {
  background(bg);
  u.move();
  u.display();
  q.display();
}

class Sentence {
  String part1, part2, solution, choice1, choice2, choice3;
  
  Sentence(String p1, String p2, String sol, String c1, String c2, String c3) {
    part1 = p1;
    part2 = p2;
    solution = sol;
    choice1 = c1;
    choice2 = c2;
    choice3 = c3;
  }
}

class Button {
  String msg;
  int xpos, ypos, xsize, ysize;
  color normal, hover;
  PFont f;
  
  Button(String m, int x, int y, int xs, int ys, color norm, color hov) {
    msg = m;
    xpos = x;
    ypos = y;
    xsize = xs;
    ysize = ys;
    normal = norm;
    hover = hov;
    f = createFont("Georgia", 20);
    textFont(f);
  }
  
  void display() {
    if(mouseX >= xpos && mouseX <= (xpos + xsize) && mouseY >= ypos && mouseY <= (ypos + ysize)) {
      fill(hover);
    }
    else {
      fill(normal);
    }
    stroke(0);
    rect(xpos, ypos, xsize, ysize, 10);

    fill(255);
    textAlign(CENTER);
    text(msg, xpos, ypos + 4, xsize, ysize);
  }
}

class Quiz {
  ArrayList<Sentence> list;
  Button b1, b2, b3, b4;
  
  Quiz() {
    list = new ArrayList<Sentence>();
    b1 = new Button("has been eaten", 10, height - 45, 300, 32, color(30), color(100));
    b2 = new Button("is being eaten", 10, height - 87, 300, 32, color(30), color(100));
    b3 = new Button("will be eaten", width - 310, height - 45, 300, 32, color(30), color(100));
    b4 = new Button("were being eaten", width - 310, height - 87, 300, 32, color(30), color(100));
    // Sentences here
    list.add(new Sentence("I", "nice", "am", "be", "are", "to be"));
  }
  
  Sentence getSentence(int i) {
    return list.get(i);
  }
  
  void display() {
    b1.display();
    b2.display();
    b3.display();
    b4.display();
  }
}

class Ufo {
  PImage[] images;
  int xpos, imageCount, frame, padding, speed;
  boolean toRight;
  
  Ufo(String imagePrefix, int count) {
    imageCount = count;
    images = new PImage[imageCount];
    
    for(int i = 0; i < imageCount; i++) {
      String filename = imagePrefix + i + ".png";
      images[i] = loadImage(filename);
    }
    
    padding = 20;
    xpos = padding + 1;
    speed = 1;
    toRight = true;
  }
  
  void display() {
    frame = (frame + 1) % imageCount;
    image(images[frame], xpos, 15);
  }
  
  void move() {
    if(toRight) {
      xpos += speed;
      if(xpos >= width - 53 - padding) toRight = false; //53 is image width
    }
    else {
      xpos -= speed;
      if(xpos <= padding) toRight = true;
    }
  }
}
