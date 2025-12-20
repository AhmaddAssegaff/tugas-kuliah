import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class SmallApple here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class GreenApple extends Food {
    /**
     * Act - do whatever the SmallApple wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    @Override
    protected void setup() {
        appleValue = 2;
        size = MyWorld.GRID;
        image = "green-apple.png";
    }
    public void act() {
        // Add your action code here.
    }
}
