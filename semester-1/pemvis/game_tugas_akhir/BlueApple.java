import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class PoisonApple here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class BlueApple extends Food {
    /**
     * Act - do whatever the PoisonApple wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    @Override
    protected void setup() {
        appleValue = -1;
        size = MyWorld.GRID;
        image = "blue-apple.png";
    }
    public void act() {
        // Add your action code here.
    }
}
