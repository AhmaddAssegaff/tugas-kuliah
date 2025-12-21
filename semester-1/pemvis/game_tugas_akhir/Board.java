import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Board here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Board extends Actor
{
    /**
     * Act - do whatever the Board wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    protected int fontSize = 28;
    protected Color textColor = Color.WHITE;
    
   protected void drawBorad(String text) {
        GreenfootImage img = new GreenfootImage(
            text,
            fontSize,
            textColor,
            new Color(0, 0, 0, 0)
        );
        setImage(img);
    }
}
