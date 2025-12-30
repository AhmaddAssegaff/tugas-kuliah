import greenfoot.*;
import java.util.LinkedList;

/**
 * Write a description of class Snake here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */

public class Snake {
    private static final int MOVE_DELAY = 7;

    private final SnakeHead head;
    private final LinkedList<SnakeBody> bodySegments = new LinkedList<>();
    private final MyWorld world;

    private int directionX = MyWorld.GRID;
    private int directionY = 0;
    private int moveFrameCounter = 0;

    public Snake(MyWorld world, int startX, int startY) {
        this.world = world;
        head = new SnakeHead();
        world.addObject(head, startX, startY);
    }

    public void act() {
        handleInput();

        if (++moveFrameCounter >= MOVE_DELAY) {
            moveFrameCounter = 0;
            updateSnake();
        }
    }

    private void updateSnake() {
        int nextHeadX = head.getX() + directionX;
        int nextHeadY = head.getY() + directionY;

        if (willCollide(nextHeadX, nextHeadY)) {
            world.gameOver();
            return;
        }

        moveHeadAndBody(nextHeadX, nextHeadY);
        handleFoodCollision();
    }

    private void handleInput() {
        if (Greenfoot.isKeyDown("up") && directionY == 0) {
            setDirection(0, -MyWorld.GRID);
        } else if (Greenfoot.isKeyDown("down") && directionY == 0) {
            setDirection(0, MyWorld.GRID);
        } else if (Greenfoot.isKeyDown("left") && directionX == 0) {
            setDirection(-MyWorld.GRID, 0);
        } else if (Greenfoot.isKeyDown("right") && directionX == 0) {
            setDirection(MyWorld.GRID, 0);
        }
    }

    private void setDirection(int x, int y) {
        directionX = x;
        directionY = y;
    }

    private void moveHeadAndBody(int newHeadX, int newHeadY) {
        int previousX = head.getX();
        int previousY = head.getY();

        head.setLocation(newHeadX, newHeadY);

        for (SnakeBody bodyPart : bodySegments) {
            int tempX = bodyPart.getX();
            int tempY = bodyPart.getY();

            bodyPart.setLocation(previousX, previousY);

            previousX = tempX;
            previousY = tempY;
        }
    }

    private void handleFoodCollision() {
        Food food = head.getIntersectingFood();
        if (food == null) return;

        int appleValue = food.getAppleValue();
        world.removeObject(food);

        if (appleValue > 0) {
            growBody(appleValue);
        } else {
            shrinkBody(-appleValue);
        }

        world.addScore(appleValue);
        world.maintainFood();
        world.checkWinCondition();
    }

    private void growBody(int segmentsToAdd) {
        for (int i = 0; i < segmentsToAdd; i++) {
            SnakeBody newBodyPart = new SnakeBody();

            int spawnX;
            int spawnY;

            if (bodySegments.isEmpty()) {
                spawnX = head.getX() - directionX;
                spawnY = head.getY() - directionY;
            } else {
                SnakeBody tail = bodySegments.getLast();
                spawnX = tail.getX();
                spawnY = tail.getY();
            }

            world.addObject(newBodyPart, spawnX, spawnY);
            bodySegments.add(newBodyPart);
        }
    }

    private void shrinkBody(int segmentsToRemove) {
        while (segmentsToRemove-- > 0 && !bodySegments.isEmpty()) {
            world.removeObject(bodySegments.removeLast());
        }
    }

    private boolean willCollide(int x, int y) {
        return hitWall(x, y) || hitOwnBody(x, y);
    }

    private boolean hitWall(int x, int y) {
        return x < 0 || x >= world.getWidth()
            || y < 0 || y >= world.getHeight();
    }

    private boolean hitOwnBody(int x, int y) {
        for (SnakeBody bodyPart : bodySegments) {
            if (bodyPart.getX() == x && bodyPart.getY() == y) {
                return true;
            }
        }
        return false;
    }
}

