/**
 * Left turn arrow to be appended to messages.
 */
SPIN_LEFT = ' \u21BA';

/**
 * Left turn arrow to be appended to messages.
 */
SPIN_RIGHT = ' \u21BB';

ACTION_HUE = 160;
CONDITIONAL_HUE = 220;
LOOPS_HUE = 300;


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
      "colour": ACTION_HUE,
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
    this.setColour(ACTION_HUE);
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

//IF
Blockly.Blocks['maze_if'] = {
  /**
   * Block for 'if' conditional if there is a path.
   * @this Blockly.Block
   */
  init: function() {
    var DIRECTIONS =
        [['Si hay Pared adelante', 'IsWallAhead'],
         ['Si hay Camino adelante', 'IsPathAhead'],
         ['Si hay Agujero adelante', 'IsHoleAhead']];
    // Append arrows to direction messages.
    this.setColour(CONDITIONAL_HUE);
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown(DIRECTIONS), 'DIR');
    this.appendStatementInput('DO')
        .appendField('Hacer');
    this.setTooltip("Hacer una accion si se cumple la condicion indicada");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
  }
};

Blockly.JavaScript['maze_if'] = function(block) {
  // Generate JavaScript for 'if' conditional if there is a path.
  var argument = block.getFieldValue('DIR') + "()"
  var branch = Blockly.JavaScript.statementToCode(block, 'DO');
  var code = 'if (' + argument + ') {\n' + branch + '}\n';
  return code;
};

//If-Else
	
Blockly.Blocks['maze_ifElse'] = {
  /**
   * Block for 'if/else' conditional if there is a path.
   * @this Blockly.Block
   */
  init: function() {
    var DIRECTIONS =
        [['Si hay Pared adelante', 'IsWallAhead'],
         ['Si hay Camino adelante', 'IsPathAhead'],
         ['Si hay Agujero adelante', 'IsHoleAhead']];
    // Append arrows to direction messages.
    this.setColour(CONDITIONAL_HUE);
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown(DIRECTIONS), 'DIR');
    this.appendStatementInput('DO')
        .appendField('Hacer');
    this.appendStatementInput('ELSE')
        .appendField('Si no hacer');
	this.setTooltip("Hacer una accion si se cumple la condicion indicada. Si no, hacer lo que esta debajo");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
  }
};

Blockly.JavaScript['maze_ifElse'] = function(block) {
  // Generate JavaScript for 'if/else' conditional if there is a path.
  var argument = block.getFieldValue('DIR') + "()";
  var branch0 = Blockly.JavaScript.statementToCode(block, 'DO');
  var branch1 = Blockly.JavaScript.statementToCode(block, 'ELSE');
  var code = 'if (' + argument + ') {\n' + branch0 +
             '} else {\n' + branch1 + '}\n';
  return code;
};

Blockly.Blocks['maze_forever'] = {
  /**
   * Block for repeat loop.
   * @this Blockly.Block
   */
  init: function() {
    this.setColour(LOOPS_HUE);
    this.appendDummyInput()
        .appendField("Hasta terminar")
    this.appendStatementInput('DO')
        .appendField("Hacer");
    this.setPreviousStatement(true);
    this.setTooltip("Hacer hasta terminar el juego");
  }
};

Blockly.JavaScript['maze_forever'] = function(block) {
  // Generate JavaScript for repeat loop.
  var branch = Blockly.JavaScript.statementToCode(block, 'DO');
  if (Blockly.JavaScript.INFINITE_LOOP_TRAP) {
    branch = Blockly.JavaScript.INFINITE_LOOP_TRAP.replace(/%1/g,
        '\'block_id_' + block.id + '\'') + branch;
  }
  return 'while (NotFinished()) {\n' + branch + '}\n';
};
