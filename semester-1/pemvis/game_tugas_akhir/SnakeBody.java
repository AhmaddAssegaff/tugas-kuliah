import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class SnakeBody here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class SnakeBody extends Actor {
    /**
     * Act - do whatever the SnakeBody wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public SnakeBody() {
        GreenfootImage img = new GreenfootImage(MyWorld.GRID, MyWorld.GRID);
        img.setColor(Color.GREEN);
        img.fill();
        setImage(img);
    }
}