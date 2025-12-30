import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class TimerBoard here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class TimerBoard extends Board {
    private int time = 0;
    private int frameCounter = 0;

    public TimerBoard() {
        updateBoardText("Time", 0);
    }

    public void act() {
        MyWorld world = (MyWorld) getWorld();
        if (world.isGameOver() || world.isGameWin()) return;

        frameCounter++;
        if (frameCounter % 60 == 0) {
            time++;
            updateBoardText("Time", time);
        }
    }

    public int getTime() {
        return time;
    }
}
