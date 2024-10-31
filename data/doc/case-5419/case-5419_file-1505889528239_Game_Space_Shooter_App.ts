declare var game: Phaser.Game;
declare var menuMusic: Phaser.Sound;
declare var gameMusic: Phaser.Sound;

/**
 * @description Class creating the game canvas and the states of the game
 */
class App {
    constructor() {
        game = new Phaser.Game(512, 910, Phaser.AUTO, 'content', { create: this.create });
        game.stage = new Phaser.Stage(game);
    }
    /**
     * @description Called after the constructor
     */
    create() {
        game.scale.scaleMode = Phaser.ScaleManager.EXACT_FIT;

        game.physics.startSystem(Phaser.Physics.ARCADE); // Start the arcade physics system

        // Add the various states the game goes through
        game.state.add("Preload", Preloader);
        game.state.add("Start", StartState);
        game.state.add("Tutorial", TuorialState);
        game.state.add("Menu", MenuState);
        game.state.add("Game", GameState);
        game.state.add("GameOver", GameOver);
        // Start the preload state
        game.state.start("Preload");
    }
}

window.onload = () => {
    var app = new App();
};