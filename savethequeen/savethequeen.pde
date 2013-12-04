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

PImage bg;
Ufo u;

void setup() {
  size(640, 480);
  frameRate(60);
  bg = loadImage("img/background.png");
  u = new Ufo("img/ufo/ufo_", 12);  
}

void draw() {
  background(bg);
  u.move();
  u.display();
}
