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

    private static final int UI_Y = 25;
    private static final int SCORE_X = 300;
    private static final int TIMER_X = 450;

    private enum GameState {
        PLAYING,
        WIN,
        GAME_OVER
    }

    private GameState gameState = GameState.PLAYING;

    private int score = 0;

    private Snake snake;
    private TimerBoard timerBoard;
    private ScoreBoard scoreBoard;

    public MyWorld() {
        super((Y_SCREEN / GRID) * GRID, (X_SCREEN / GRID) * GRID, 1);
        
        prepareWorld();
    }

    public void act() {
        if (gameState != GameState.PLAYING) return;
        
        snake.act();
        maintainFood();
    }

    @Override
    public void started() {
        for (int i = 0; i < MIN_FOOD_EXISTS; i++) {
            maintainFood();
        }
    }

    public void gameWin() {
        if (gameState == GameState.WIN) return;
        gameState = GameState.WIN;
        showGameWinBoard();
    }

    public void gameOver() {
        if (gameState == GameState.GAME_OVER) return;
        gameState = GameState.GAME_OVER;
        showGameOverBoard();
    }

    public void checkWinCondition() {
        if (gameState != GameState.PLAYING) return;
        if (isSnakeFull()) {
            gameWin();
        }
    }

    public void addScore(int amount) {
        score += amount;
        if (score < 0) score = 0;
        scoreBoard.setScore(score);
    }

    public int getScore() {
        return score;
    }

    public boolean isGameOver() {
        return gameState == GameState.GAME_OVER;
    }

    public boolean isGameWin() {
        return gameState == GameState.WIN;
    }

    public int getLengthSnake() {
        return getObjects(SnakeBody.class).size() + 1;
    }

    public int getTotalCells() {
        return (getWidth() / GRID) * (getHeight() / GRID);
    }

    public boolean isSnakeFull() {
        return getLengthSnake() >= getTotalCells();
    }

    public void maintainFood() {
        int targetMaxFood = getMaxFoodBasedOnSnakeLength();
        int totalFood = getObjects(Food.class).size();

        if (totalFood < targetMaxFood) {
            int occupiedCells = getLengthSnake() + totalFood;
            if (occupiedCells >= getTotalCells()) return;
            spawnFoodOnce();
        }
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

    private int getMaxFoodBasedOnSnakeLength() {
        int snakeLength = getLengthSnake();
        int maxFood = MIN_FOOD_EXISTS + ((snakeLength - 1) * FOOD_GROWTH_FACTOR);
        return Math.min(maxFood, MAX_FOOD);
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

    public boolean isCellBlocked(int x, int y) {
        return !getObjectsAt(x, y, Actor.class).isEmpty();
    }

    private void prepareWorld() {
        GreenfootImage bg = new GreenfootImage("bg-snake.jpg");
        bg.scale(getWidth(), getHeight());
        setBackground(bg);
        
        int startX = (getWidth() / 2 / GRID) * GRID + GRID / 2;
        int startY = (getHeight() / 2 / GRID) * GRID + GRID / 2;
        snake = new Snake(this, startX, startY);
        
        timerBoard = new TimerBoard();
        scoreBoard = new ScoreBoard();

        addObject(scoreBoard, SCORE_X, UI_Y);
        addObject(timerBoard, TIMER_X, UI_Y);
    }

    private void showGameWinBoard() {
        addObject(new GameWinBoard(), getWidth() / 2, getHeight() / 2);
    }

    private void showGameOverBoard() {
        addObject(new GameOverBoard(), getWidth() / 2, getHeight() / 2);
    }
}
