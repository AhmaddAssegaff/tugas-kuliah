import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World {
    

    public static final int GRID = 25;
    private static final int MIN_FOOD = 3;
    private static final int MAX_FOOD = 36;
    private static final int FOOD_GROWTH_FACTOR = 3;
    private static final int RED_APPLE_PERCENT = 50;
    private static final int BLUE_APPLE_PERCENT = 35;
    
    public MyWorld() {    
        super((900 / GRID) * GRID, (600 / GRID) * GRID, 1);

        GreenfootImage bg = new GreenfootImage("bg-snake.jpg");
        bg.scale(getWidth(), getHeight());
        setBackground(bg);
    }
    
    public int getLengthSnake() {
      return getObjects(SnakeBody.class).size() + 1; 
    }

    private int getDynamicMaxFood() {
      int length = getLengthSnake();
      int maxFood = MIN_FOOD + (length * FOOD_GROWTH_FACTOR);

      if (maxFood > MAX_FOOD) {
          maxFood = MAX_FOOD;
      }

      return maxFood;
    }

    @Override
    public void started() {
        for (int i = 0; i < MIN_FOOD; i++) {
            spawnFood();
        }
    }

    public boolean isCellBlocked(int x, int y) {
        return !getObjectsAt(x, y, Snake.class).isEmpty();
    }

    private Food createRandomFood() {
        int spawnChance = Greenfoot.getRandomNumber(100);

        if (spawnChance < RED_APPLE_PERCENT) {
            return new RedApple();
        }
        if (spawnChance < RED_APPLE_PERCENT + BLUE_APPLE_PERCENT) {
            return new BlueApple();

        }
        return new GreenApple();
    }

    public void spawnFood() {
        if (getObjects(Food.class).size() >= getDynamicMaxFood()) return;

        int cols = getWidth() / GRID;
        int rows = getHeight() / GRID;

        for (int i = 0; i < 10; i++) {
            int x = Greenfoot.getRandomNumber(cols) * GRID + GRID / 2;
            int y = Greenfoot.getRandomNumber(rows) * GRID + GRID / 2;

            if (!isCellBlocked(x, y)) {
                addObject(createRandomFood(), x, y);
                break;
            }
        }
    }
}
