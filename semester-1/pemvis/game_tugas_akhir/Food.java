import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)
/**
 * Write a description of class Food here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public abstract class Food extends Actor {
    protected int effect;     // +1, +3, -2
    protected int size;       // ukuran grid
    protected String image;   // nama file
    
    /**
     * Constructor for objects of class Food
     */
    protected abstract void setup();
    public Food() {
        setup();
        prepareImage();
    }
    private void prepareImage() {
        GreenfootImage img = new GreenfootImage(image);
        img.scale(size, size);
        setImage(img);
    }
    public int getEffect() {
        return effect;
    }
}
