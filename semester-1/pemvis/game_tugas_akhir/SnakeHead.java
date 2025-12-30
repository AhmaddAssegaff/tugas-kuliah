import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class HeadSnake here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class SnakeHead extends Actor {
    /**
     * Act - do whatever the HeadSnake wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    private static final Color COLOR = Color.RED;
    
    public SnakeHead() {
        GreenfootImage img = new GreenfootImage(MyWorld.GRID, MyWorld.GRID);
        img.setColor(COLOR);
        img.fill();
        setImage(img);
    }
    
    public Food getIntersectingFood() {
        return (Food) getOneIntersectingObject(Food.class);
    }
    
    public boolean hitBody() {
        return getOneIntersectingObject(SnakeBody.class) != null;
    }
}