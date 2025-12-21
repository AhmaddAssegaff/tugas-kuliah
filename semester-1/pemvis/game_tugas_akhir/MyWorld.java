import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class MyWorld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class MyWorld extends World {
    private static final int X_SCREEN = 600;
    private static final int Y_SCREEN = 900;
    
    public static final int GRID = 25;
    
    private static final int MIN_FOOD_EXISTS = 2;
    private static final int MAX_FOOD = (X_SCREEN / GRID) * (Y_SCREEN / GRID);
    
    private static final int FOOD_GROWTH_FACTOR = 2;
    private static final int RED_APPLE_PERCENT = 50;
    private static final int BLUE_APPLE_PERCENT = 10;
    
    Snake snake = new Snake();
    TimerBoard timerBoard = new TimerBoard();
    ScoreBoard scoreBoard = new ScoreBoard();
    
    public MyWorld() {    
        super((Y_SCREEN / GRID) * GRID, (X_SCREEN / GRID) * GRID, 1);

        GreenfootImage bg = new GreenfootImage("bg-snake.jpg");
        bg.scale(getWidth(), getHeight());
        setBackground(bg);
        
        addObject(snake, getWidth() / 2, getHeight() / 2);
        addObject(timerBoard, 450, 25);
        addObject(scoreBoard, 300, 25);
    }
    
    public void act() {
        maintainFood();
    }
    
    @Override
    public void started() {
        for (int i = 0; i < MIN_FOOD_EXISTS; i++) {
            maintainFood();
        }
    }
    
    public int getLengthSnake() {
      return getObjects(SnakeBody.class).size() + 1; 
    }

    private int getDynamicMaxFood() {
      int snakeLength = getLengthSnake();
      int maxFood = MIN_FOOD_EXISTS + ((snakeLength - 1) * FOOD_GROWTH_FACTOR);
      
      if (maxFood > MAX_FOOD) {
          maxFood = MAX_FOOD;
      }

      return maxFood;
    }
    
    public void spawnFoodOnce() {
      int cols = getWidth() / GRID;
      int rows = getHeight() / GRID;

      for (int i = 0; i < 10; i++) {
          int x = Greenfoot.getRandomNumber(cols) * GRID + GRID / 2;
          int y = Greenfoot.getRandomNumber(rows) * GRID + GRID / 2;

          if (!isCellBlocked(x, y)) {
              addObject(createRandomFood(), x, y);
              return; 
          }
      }
    }

    public void maintainFood() {
      int targetMaxFood = getDynamicMaxFood();
      int totalCells = (getWidth() / GRID) * (getHeight() / GRID);
      int totalFood = getObjects(Food.class).size();
      
      if (totalFood < targetMaxFood) {
          int occupiedCells = getLengthSnake() + totalFood;                                                                                                                                  
          if (occupiedCells >= totalCells) {
              return;
          }
          spawnFoodOnce();
      }
    } 

    public boolean isCellBlocked(int x, int y) {
        if (!getObjectsAt(x, y, Snake.class).isEmpty()) return true;
        if (!getObjectsAt(x, y, SnakeBody.class).isEmpty()) return true; 
        if (!getObjectsAt(x, y, SnakeHead.class).isEmpty()) return true;  
        if (!getObjectsAt(x, y, Food.class).isEmpty()) return true;
        
        return false;
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
}
