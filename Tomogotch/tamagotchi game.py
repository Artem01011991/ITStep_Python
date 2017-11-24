from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.uix.button import Button


class TamagotchiGame(Widget):
    critter_hungre = NumericProperty(0)  # Initial values for
    critter_health = NumericProperty(100)# displaying
    critter_poopy = NumericProperty(0)
    poopy_cur = True  # tracker for creating button
# Core of the game. Tied to time
    def update(self, tb):
        def cleare_poopy(tb):
            nonlocal btr
            self.poopy_cur = True

            self.remove_widget(btr)
            self.critter_poopy = 0

        if self.critter_hungre == 100: # Critter is hungry
            self.critter_health -= 1
            self.critter_poopy += 1
        else:
            self.critter_poopy += 1
            self.critter_hungre += 1

        if self.critter_poopy >= 100: # Critter needs a toilet
            self.critter_health -= 1
            if self.poopy_cur:
                self.poopy_cur = False

                btr = Button(background_normal='poopy.png', center=(100, 250), size=(150, 200), on_press=cleare_poopy)
                self.add_widget(btr)
        elif self.critter_health < 100 and self.critter_hungre != 100:
            self.critter_health += 1

        if self.critter_health == 0:
            App.get_running_app().stop()

    def feed_critter(self):
        self.critter_hungre -= 30
        self.critter_poopy += 10
        if self.critter_hungre < 0:
            self.critter_hungre = 0


class TamagotchiApp(App):
    def build(self):
        def exit_game(tb):
            App.get_running_app().stop()

        game = TamagotchiGame()
        btn2 = Button(text='Exit', on_release=exit_game)
        game.add_widget(btn2)

        Clock.schedule_interval(game.update, 1.0) # Tied to update function. Represents changing of critter's values

        return game


if __name__ == '__main__':
    TamagotchiApp().run()