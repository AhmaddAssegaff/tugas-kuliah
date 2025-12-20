import greenfoot.*;
import java.util.LinkedList;

/**
 * Write a description of class Snake here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

public class Snake extends Actor {
  private static final int MOVE_DELAY_FRAMES = 7;
  private static final Color HEAD_COLOR = Color.RED;
    
  private LinkedList<SnakeBody> bodyList = new LinkedList<>();

  private int moveCounter = 0;
  private int directionX = MyWorld.GRID;
  private int directionY = 0;

  public Snake() {
      GreenfootImage headImage = new GreenfootImage(MyWorld.GRID, MyWorld.GRID);
      headImage.setColor(HEAD_COLOR);
      headImage.fill();
      setImage(headImage);
  }

  public void act() {
      handleInput();
      moveWithDelay();
  } 

  private void handleInput() {
      if (Greenfoot.isKeyDown("up") && directionY == 0) {
          directionX = 0;
          directionY = -MyWorld.GRID;
      } else if (Greenfoot.isKeyDown("down") && directionY == 0) {
          directionX = 0;
          directionY = MyWorld.GRID;
      } else if (Greenfoot.isKeyDown("left") && directionX == 0) {
          directionX = -MyWorld.GRID;
          directionY = 0;
      } else if (Greenfoot.isKeyDown("right") && directionX == 0) {
          directionX = MyWorld.GRID;
          directionY = 0;
      }
  }

  private void moveWithDelay() {
      moveCounter++;
      if (moveCounter >= MOVE_DELAY_FRAMES) {
          moveCounter = 0;
          moveSnake();
      }
  }

  private void moveSnake() {
      int previousHeadX = getX();
      int previousHeadY = getY();

      setLocation(getX() + directionX, getY() + directionY);

      moveBody(previousHeadX, previousHeadY);

      checkAppleCollision();
  }

  private void moveBody(int prevX, int prevY) {
      for (SnakeBody part : bodyList) {
          int tempX = part.getX();
          int tempY = part.getY();
          part.setLocation(prevX, prevY);
          prevX = tempX;
          prevY = tempY;
      }
  }

  private void checkAppleCollision() {
      Food apple = (Food) getOneIntersectingObject(Food.class);
      if (apple == null) return;

      int appleEffect = apple.getEffect();
      getWorld().removeObject(apple);

      if (appleEffect > 0) {
          growBody(appleEffect);
      } else if (appleEffect < 0) {
          shrinkBody(-appleEffect);
      }

      ((MyWorld)getWorld()).maintainFood();
  }

  private void growBody(int count) {
      for (int i = 0; i < count; i++) {
          SnakeBody newBody = new SnakeBody();
          if (bodyList.isEmpty()) {
              getWorld().addObject(newBody, getX(), getY());
          } else {
              SnakeBody tail = bodyList.getLast();
              getWorld().addObject(newBody, tail.getX(), tail.getY());
          }
          bodyList.addLast(newBody);
      }
  }

  private void shrinkBody(int count) {
      for (int i = 0; i < count; i++) {
          if (!bodyList.isEmpty()) {
              SnakeBody tail = bodyList.removeLast();
              getWorld().removeObject(tail);
          }
      }
  }
}
