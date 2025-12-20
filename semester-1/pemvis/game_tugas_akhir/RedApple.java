import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class BigApple here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class RedApple extends Food {
    /**
     * Act - do whatever the BigApple wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    @Override
    protected void setup() {
        appleValue = 1;
        size = MyWorld.GRID;
        image = "red-apple.png";
    }   
    public void act() {
        // Add your action code here.
    }
}
