//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#ytd4gg
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


//set_current_value
Blockly.Blocks['set_current_digit'] = {
  init: function() {
    this.appendValueInput("arg")
        .setCheck(null)
        .appendField("Asignar digito actual");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Asignar el valor del digito actual");
 this.setHelpUrl("\"\"");
  }
};

Blockly.JavaScript['set_current_digit'] = function(block) {
  var value_arg = Blockly.JavaScript.valueToCode(block, 'arg', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'SetCurrentDigit(' + value_arg + ');\n';
  return code;
};

Blockly.Blocks['get_current_digit'] = {
  /**
   * Block for moving forward.
   * @this Blockly.Block
   */
  init: function() {
    this.jsonInit({
	  "type": "get_current_digit",
	  "message0": "Digito Actual",
	  "output": "Number",
	  "colour": 230,
	  "tooltip": "asd",
	  "helpUrl": ""
	});
  }
};

Blockly.JavaScript['get_current_digit'] = function(block) {
  // Generate JavaScript for moving forward.
	var code = 'GetCurrentDigit()';
	return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.Blocks['get_last_digit'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Ultimo Digito Ingresado");
    this.setColour(230);
	 this.setTooltip("Obtener el ultimo digito ingresado. En caso de no existir, devuelve 0");
	 this.setHelpUrl("");
  }
};

Blockly.JavaScript['get_last_digit'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'GetLastDigit()';
  return code;
};

Blockly.Blocks['get_antelast_digit'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Anteultimo digito ingresado");
    this.setColour(230);
 this.setTooltip("Obtener el anteultimo digito ingresado. En caso de no existir, devuelve 0");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['get_antelast_digit'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'GetAntelastDigit()';
  return code;
};

Blockly.Blocks['input_count'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Cantidad digitos ingresados");
    this.setColour(230);
 this.setTooltip("Obtener la cantidad de digitos ingresados");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['input_count'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'GetInputCount()';
  return code;
};

Blockly.Blocks['multiply'] = {
  init: function() {
    this.appendValueInput("arg1")
        .setCheck("Number")
        .appendField("Multiplicar");
    this.appendValueInput("arg2")
        .setCheck("Number")
        .appendField("x");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(0);
 this.setTooltip("asd");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['multiply'] = function(block) {
  var value_arg1 = Blockly.JavaScript.valueToCode(block, 'arg1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_arg2 = Blockly.JavaScript.valueToCode(block, 'arg2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_arg1 + ' * ' + value_arg2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.Blocks['sum'] = {
  init: function() {
    this.appendValueInput("arg1")
        .setCheck("Number")
        .appendField("Sumar");
    this.appendValueInput("arg2")
        .setCheck("Number")
        .appendField("+");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(0);
 this.setTooltip("Suma 2 numeros");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['sum'] = function(block) {
  var value_arg1 = Blockly.JavaScript.valueToCode(block, 'arg1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_arg2 = Blockly.JavaScript.valueToCode(block, 'arg2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_arg1 + ' + ' + value_arg2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.Blocks['subtract'] = {
  init: function() {
    this.appendValueInput("arg1")
        .setCheck("Number")
        .appendField("Restar");
    this.appendValueInput("arg2")
        .setCheck("Number")
        .appendField("-");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(0);
 this.setTooltip("Resta 2 numeros");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['subtract'] = function(block) {
  var value_arg1 = Blockly.JavaScript.valueToCode(block, 'arg1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_arg2 = Blockly.JavaScript.valueToCode(block, 'arg2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_arg1 + ' - ' + value_arg2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.Blocks['divide'] = {
  init: function() {
    this.appendValueInput("arg1")
        .setCheck("Number")
        .appendField("Dividir");
    this.appendValueInput("arg2")
        .setCheck("Number")
        .appendField("/");
    this.setInputsInline(true);
    this.setOutput(true, "Number");
    this.setColour(0);
 this.setTooltip("Divide 2 numeros");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['divide'] = function(block) {
  var value_arg1 = Blockly.JavaScript.valueToCode(block, 'arg1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_arg2 = Blockly.JavaScript.valueToCode(block, 'arg2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_arg1 + ' / ' + value_arg2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.Blocks['while_not_finished'] = {
  init: function() {
    this.appendStatementInput("body")
        .setCheck(null)
        .appendField("Hasta finalizar");
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['while_not_finished'] = function(block) {
  var statements_body = Blockly.JavaScript.statementToCode(block, 'body');
  // TODO: Assemble JavaScript into code variable.
  var code = 'while (!FinishedInputting()){ \n' + statements_body + ' }\n';
  return code;
};

Blockly.Blocks['number'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Numero");
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "Numero");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setColour(230);
 this.setTooltip("Numero");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['number'] = function(block) {
  var number_numero = block.getFieldValue('Numero');
  // TODO: Assemble JavaScript into code variable.
  var code = numero;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

Blockly.Blocks['multiply_current_digit'] = {
  init: function() {
    this.appendValueInput("arg")
        .setCheck(null)
        .appendField("Multiplicar Digito actual por ");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Multiplica el digito actual por otro numero");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['multiply_current_digit'] = function(block) {
  var value_arg = Blockly.JavaScript.valueToCode(block, 'arg', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'MultiplyCurrentDigit(' + arg + ');\n';
  return code;
};

Blockly.Blocks['add_to_current_digit'] = {
  init: function() {
    this.appendValueInput("arg")
        .setCheck(null)
        .appendField("Sumarle al digito actual ");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Suma el digito actual con otro numero");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['add_to_current_digit'] = function(block) {
  var value_arg = Blockly.JavaScript.valueToCode(block, 'arg', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'AddToCurrentDigit(' + value_arg + ');\n';
  return code;
};

Blockly.Blocks['subtract_current_digit'] = {
  init: function() {
    this.appendValueInput("arg")
        .setCheck(null)
        .appendField("Restarle al digito actual ");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Le resta el digito actual otro numero");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['subtract_current_digit'] = function(block) {
  var value_arg = Blockly.JavaScript.valueToCode(block, 'arg', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'SubtractFromCurrentDigit(' + value_arg + ');\n';
  return code;
};

Blockly.Blocks['divide_current_digit'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("Dividir al digito actual por");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Divide el digito actual por otro numero");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['divide_current_digit'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'DivideCurrentDigit(' + value_arg + ');\n';
  return code;
};

Blockly.Blocks['input_current_digit'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Confirmar Digito Actual");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Confirmar digito actual");
 this.setHelpUrl("\"\"");
  }
};

Blockly.JavaScript['input_current_digit'] = function(block) {
  // TODO: Assemble JavaScript into code variable.
  var code = 'InputCurrentDigit();\n';
  return code;
};