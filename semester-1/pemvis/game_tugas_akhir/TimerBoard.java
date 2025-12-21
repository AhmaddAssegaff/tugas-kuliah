import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class TimerBoard here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class TimerBoard extends Board
{
    /**
     * Act - do whatever the TimerBoard wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    private int time = 0;
    private int counterTime = 0;
    
    public TimerBoard() {
        drawBorad("Time: 0");
    }
    
    public void act() {
        counterTime++;
        if (counterTime % 60 == 0) {
            time++;
            drawBorad("Time: " + time + " s");
        }   
    }
    
    public int getTime() {
        return time;
    }
}
