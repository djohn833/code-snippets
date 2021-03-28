'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var FilterableProductTable = function (_React$Component) {
  _inherits(FilterableProductTable, _React$Component);

  function FilterableProductTable(props) {
    _classCallCheck(this, FilterableProductTable);

    var _this = _possibleConstructorReturn(this, (FilterableProductTable.__proto__ || Object.getPrototypeOf(FilterableProductTable)).call(this, props));

    _this.handleFilterTextChange = function (e) {
      _this.setState({ filterText: e.target.value });
    };

    _this.handleInStockOnlyChange = function (e) {
      _this.setState({ inStockOnly: e.target.checked });
    };

    _this.state = {
      filterText: 'ball',
      inStockOnly: false
    };
    return _this;
  }

  _createClass(FilterableProductTable, [{
    key: 'render',
    value: function render() {
      var products = this.props.products;
      return React.createElement(
        'div',
        null,
        React.createElement(SearchBar, {
          filterText: this.state.filterText,
          inStockOnly: this.state.inStockOnly,
          handleFilterTextChange: this.handleFilterTextChange,
          handleInStockOnlyChange: this.handleInStockOnlyChange }),
        React.createElement(ProductTable, {
          products: products,
          filterText: this.state.filterText,
          inStockOnly: this.state.inStockOnly })
      );
    }
  }]);

  return FilterableProductTable;
}(React.Component);

var SearchBar = function (_React$Component2) {
  _inherits(SearchBar, _React$Component2);

  function SearchBar() {
    _classCallCheck(this, SearchBar);

    return _possibleConstructorReturn(this, (SearchBar.__proto__ || Object.getPrototypeOf(SearchBar)).apply(this, arguments));
  }

  _createClass(SearchBar, [{
    key: 'render',
    value: function render() {
      var filterText = this.props.filterText;
      var inStockOnly = this.props.inStockOnly;
      var handleFilterTextChange = this.props.handleFilterTextChange;
      var handleInStockOnlyChange = this.props.handleInStockOnlyChange;

      return React.createElement(
        'form',
        null,
        React.createElement('input', {
          type: 'text',
          placeholder: 'Search...',
          value: filterText,
          onChange: handleFilterTextChange }),
        React.createElement(
          'p',
          null,
          React.createElement('input', {
            type: 'checkbox',
            checked: inStockOnly,
            onChange: handleInStockOnlyChange }),
          ' ',
          'Only show products in stock'
        )
      );
    }
  }]);

  return SearchBar;
}(React.Component);

var ProductTable = function (_React$Component3) {
  _inherits(ProductTable, _React$Component3);

  function ProductTable() {
    _classCallCheck(this, ProductTable);

    return _possibleConstructorReturn(this, (ProductTable.__proto__ || Object.getPrototypeOf(ProductTable)).apply(this, arguments));
  }

  _createClass(ProductTable, [{
    key: 'render',
    value: function render() {
      var filterText = this.props.filterText;
      var inStockOnly = this.props.inStockOnly;

      var rows = [];
      var currCategory = null;

      this.props.products.forEach(function (product) {
        if (inStockOnly && !product.stocked) {
          return;
        }

        if (product.name.indexOf(filterText) === -1) {
          return;
        }

        if (product.category !== currCategory) {
          currCategory = product.category;
          rows.push(React.createElement(ProductCategoryRow, { category: product.category, key: product.category }));
        }

        rows.push(React.createElement(ProductRow, { product: product, key: product.name }));
      });

      return React.createElement(
        'table',
        null,
        React.createElement(
          'thead',
          null,
          React.createElement(
            'tr',
            null,
            React.createElement(
              'th',
              null,
              'Name'
            ),
            React.createElement(
              'th',
              null,
              'Price'
            )
          )
        ),
        React.createElement(
          'tbody',
          null,
          rows
        )
      );
    }
  }]);

  return ProductTable;
}(React.Component);

var ProductCategoryRow = function (_React$Component4) {
  _inherits(ProductCategoryRow, _React$Component4);

  function ProductCategoryRow() {
    _classCallCheck(this, ProductCategoryRow);

    return _possibleConstructorReturn(this, (ProductCategoryRow.__proto__ || Object.getPrototypeOf(ProductCategoryRow)).apply(this, arguments));
  }

  _createClass(ProductCategoryRow, [{
    key: 'render',
    value: function render() {
      var category = this.props.category;
      return React.createElement(
        'tr',
        null,
        React.createElement(
          'th',
          { colSpan: '2' },
          category
        )
      );
    }
  }]);

  return ProductCategoryRow;
}(React.Component);

var ProductRow = function (_React$Component5) {
  _inherits(ProductRow, _React$Component5);

  function ProductRow() {
    _classCallCheck(this, ProductRow);

    return _possibleConstructorReturn(this, (ProductRow.__proto__ || Object.getPrototypeOf(ProductRow)).apply(this, arguments));
  }

  _createClass(ProductRow, [{
    key: 'render',
    value: function render() {
      var product = this.props.product;
      var name = product.stocked ? product.name : React.createElement(
        'span',
        { style: { color: 'red' } },
        product.name
      );

      return React.createElement(
        'tr',
        null,
        React.createElement(
          'td',
          null,
          name
        ),
        React.createElement(
          'td',
          null,
          product.price
        )
      );
    }
  }]);

  return ProductRow;
}(React.Component);

(function () {
  var PRODUCTS = [{ category: 'Sporting Goods', price: '$49.99', stocked: true, name: 'Football' }, { category: 'Sporting Goods', price: '$9.99', stocked: true, name: 'Baseball' }, { category: 'Sporting Goods', price: '$29.99', stocked: false, name: 'Basketball' }, { category: 'Electronics', price: '$99.99', stocked: true, name: 'iPod Touch' }, { category: 'Electronics', price: '$399.99', stocked: false, name: 'iPhone 5' }, { category: 'Electronics', price: '$199.99', stocked: true, name: 'Nexus 7' }];

  ReactDOM.render(React.createElement(FilterableProductTable, { products: PRODUCTS }), document.getElementById('container'));
})();