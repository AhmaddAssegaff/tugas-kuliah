import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class ScoreBoard here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class ScoreBoard extends Board
{
    /**
     * Act - do whatever the ScoreBoard wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() {
        MyWorld world = (MyWorld) getWorld();
        updatedSore(world.getLengthSnake() - 1);
    }
    
    public ScoreBoard() {
        drawBorad("Score : 0");
    }
    
    private void updatedSore(int score) {
        drawBorad("Score: " + score);
    }
}
