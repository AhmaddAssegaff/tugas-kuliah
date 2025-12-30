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
        MyWorld world = (MyWorld) getWorld();
        
        if (world.isGameOver()) return;
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
    
    private boolean hitWall(int x, int y) {
        return x < 0 || x >= getWorld().getWidth() || y < 0 || y >= getWorld().getHeight();
    }

    private boolean hitSelf(int x, int y) {
        for (SnakeBody body : bodyList) {
            if (body.getX() == x && body.getY() == y) {
                return true;
            }
        }
        return false;
    }

    private void moveSnake() {
        int nextX = getX() + directionX;
        int nextY = getY() + directionY;
    
        if (hitWall(nextX, nextY) || hitSelf(nextX, nextY)) {
            gameOver();
            return;
        }
    
        int prevX = getX();
        int prevY = getY();
    
        setLocation(nextX, nextY);
        moveBody(prevX, prevY);
    
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
        
        MyWorld world = (MyWorld) getWorld();
        int appleValue = apple.getAppleValue();
        
        getWorld().removeObject(apple);
        
        if (appleValue > 0) {
            growBody(appleValue);
        } else if (appleValue < 0) {
            shrinkBody(-appleValue);
        }
        
        world.addScore(appleValue);
        world.maintainFood();
        world.checkWinCondition();
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
    
    private void gameOver() {
        MyWorld world = (MyWorld) getWorld();
        world.gameOver();
    }
}
