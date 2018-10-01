/**
 * Left turn arrow to be appended to messages.
 */
SPIN_LEFT = ' \u21BA';

/**
 * Left turn arrow to be appended to messages.
 */
SPIN_RIGHT = ' \u21BB';

//Move Forward
Blockly.Blocks['maze_move_forward'] = {
  /**
   * Block for moving forward.
   * @this Blockly.Block
   */
  init: function() {
    this.jsonInit({
      "message0": "Avanzar",
      "previousStatement": null,
      "nextStatement": null,
      "colour": 160,
      "tooltip": "Avanzar hacia adelante"
    });
  }
};

Blockly.JavaScript['maze_move_forward'] = function(block) {
  // Generate JavaScript for moving forward.
  return 'MoveForward();\n';
};

//Spin Left
Blockly.Blocks['maze_spin'] = {
  /**
   * Block for spinning left or right.
   * @this Blockly.Block
   */
  init: function() {
    var DIRECTIONS =
        [["Girar Izquierda", 'Left'],
        ["Girar Derecha", 'Right']];
    // Append arrows to direction messages.
    DIRECTIONS[0][0] += SPIN_LEFT;
    DIRECTIONS[1][0] += SPIN_RIGHT;
    this.setColour(160);
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown(DIRECTIONS), 'DIR');
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip("Girar a la derecha o a la izquierda");
  }
};

Blockly.JavaScript['maze_spin'] = function(block) {
  // Generate JavaScript for turning left or right.
  var dir = block.getFieldValue('DIR');
  return "Spin" + dir + '();\n';
};
