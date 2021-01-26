from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game import Game
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
game = Game()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
screen.onkey(game.start_game, "space")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if not game.start_on:
        game.home_start()
    else:
        game.clear()
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            score.update_score()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
            score.reset()
            snake.reset()

        # Detect collision with the the body
        for segment in snake.segment_list[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()






screen.exitonclick()