GET_METHOD_TEMPLATE="""	/**
	 * Gets %s.
	 *
	 * @return %s
	 */
	%s get%s();"""

SET_METHOD_TEMPLATE="""	/**
	 * Sets %s.
	 *
	 * @param %s
	 *            %s
	 */
	void set%s(%s %s);"""

IS_METHOD_TEMPLATE="""	/**
	 * Checks if this is %s or not.
	 *
	 * @return {@code true} if this is %s
	 */
	%s is%s();"""

INTERFACE_TEMPLATE="""package com.wongnai.domain.model.%s;

/**
 * %s.
 *
 * @author %s
 */
public interface %s extends %s<%s> {
%s
}
"""

IMPLEMENT_TEMPLATE="""package com.wongnai.domain.model.%s.internal;

/**
 * Default implementation of {@link %s}.
 *
 * @author %s
 */
public class %sImpl extends %s<%s> implements %s {
	private static final long serialVersionUID = 1L;
%s
%s
}
"""

GET_METHOD_IMPL_TEMPLATE="""	/**
	 * {@inheritDoc}
	 */
	@Override
	public %s get%s() {
		return %s;
	}"""

SET_METHOD_IMPL_TEMPLATE="""	/**
	 * {@inheritDoc}
	 */
	@Override
	public void set%s(%s %s) {
		this.%s = %s;
	}"""

IS_METHOD_IMPL_TEMPLATE="""	/**
	 * {@inheritDoc}
	 */
	@Override
	public %s get%s() {
		return %s;
	}"""
